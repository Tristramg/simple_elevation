#coding=utf8

# Licence : do whatever you want with it. Pay me a beer if you believe it was usefull
# Starts a minimal webservice that returns an elevation profile between two coordinates
# By default it runs on localhost:8080
# Only one api is implemented : /profile?lon1=&lat1=&lon2=&lat2=
# Bad news, you have to specify the region you want to cover manually

# Choose one: "Africa", "Australia", "Eurasia", "Islands", "North_America", "South_America"
region = 'Eurasia'

import json
import wsgiref.simple_server as server
from cgi import parse_qs, escape
from profile import steps

def profile(environ, start_response):
    parameters = parse_qs(environ.get('QUERY_STRING', ''))
    if "lon1" in parameters and "lat1" in parameters and "lon2" in parameters and "lat2" in parameters:
        response_headers = [('Content-Type', 'application/json')]
        start_response('200 OK', response_headers)
        res = steps(float(parameters['lon1'][0]),float(parameters['lat1'][0]), float(parameters['lon2'][0]), float(parameters['lat2'][0]), region)
        if 'callback' in parameters: #support jsonp
            return [parameters['callback'][0] + '(' + json.dumps(res) + ')']
        else:
            return [json.dumps(res)]
    else:
        response_headers = [('Content-Type', 'text/plain')]
        start_response('200 OK', response_headers)
        return ["missing at least one of the following arguments : lon1, lat1, lon2, lat2"]


def application(environ, start_response):
    if environ['PATH_INFO'] == "/profile":
        return profile(environ, start_response)
    else:
        response_headers = [('Content-Type', 'text/plain')]
        start_response('404 Not Found', response_headers)
        return ["Get Away!"]


httpd = server.make_server('0.0.0.0', 8080, application)
httpd.serve_forever()
