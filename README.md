simple_elevation
================

Python library to get the elevation of some point on earth and elevation profiles.

The data is downloaded from the NASA server www2.jpl.nasa.gov/srtm/ and kept in cache. So the first request will need some time.
The next one will be significantly faster.
Each download is a tile that covers a 1 degree wide surface.

One anoying thing is that the tiles are separated in different folders. This is why you have to specify the regions by hand.
The regions are: "Africa", "Australia", "Eurasia", "Islands", "North_America" and "South_America".

How to use this library: three files with three different services.

elevation.py
------------

Gets you the elevation of some point on earth :

    import elevation
    el = elevation.ElevationData('Eurasia')
    print el.altitude(lon=2.4, lat=48.86)

profile.py
----------

Gets you an elevation profile between two points :

    from profile import steps
    print steps(2.4, 48.86, 2.41, 48.82, 'Eurasia')

The default resolution is 1200 points per degree. Try not to ask more than one degree. You can, but I’m not responsible.

webservice.py
-------------

Braindead webservice that could be handy if you want to display elevation data on a map (but it supports jsonp).

    python webservice.py &
    curl "http://localhost:8080/profile?lon1=2.4&lat1=48.86&lon2=2.41&lat2=48.82"
