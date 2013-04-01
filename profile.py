#coding=utf8
import elevation

def get_afine_equation(x1, y1, x2, y2):
    """
    Oh god… afine functions… back to junior high
    We want to a function that computes y = ax + b
    a and b are computed from the given coordinates
    """
    def f(x):
        a = (y1 - y2) / (x1 - x2)
        b = (y1 + y2 - a * (x1 + x2)) / 2
        return a * x + b

    return f

def steps(lon1, lat1, lon2, lat2, region = 'Eurasia', points_per_degree = 1200):
    """
    We have two points, and we want to get as many intermediate points as possible
    But with at most 1200 points/degree as it is the elevation data resolution
    """ 
    nb_steps = points_per_degree*max(abs(lon1-lon2), abs(lat1-lat2))
    print nb_steps
    step = abs(lon1 - lon2) / nb_steps
    f = get_afine_equation(lon1, lat1, lon2, lat2)

    current_lon = min(lon1,lon2)
    end_lon = max(lon1,lon2)
    el = elevation.ElevationData(region)
    result = []
    while current_lon < end_lon:
        lat = f(current_lon)
        result.append( {'lon': current_lon, 'lat': lat, 'elevation': el.altitude(lat, current_lon)} )
        current_lon += step
    return result


