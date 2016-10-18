#!/usr/bin/env python

"""
    get_wind_data.py: using strava start and end latitude / longitude, output wind speed in mph and wind direction
                      in degrees from nearest weather underground station.

    Initial Implementation: 09/06/2016 [William Golembieski]
    Last Modification: 10/17/2016 [William Golembieski]

"""

from urllib2 import urlopen
from json import loads
from api_key_data import WU_API_KEY

__author__ = "William Golembieski"
__copyright__ = "Copyright 2016, Strava AeroLabs"
__credits__ = ["William Golembieski"]
__license__ = "GNU General Public License v3.0"
__version__ = "1.0.0"
__maintainer__ = "William Golembieski"
__email__ = "BillGolembieski@projectu23.com"
__status__ = "Production"


def get_wind(user_lat, user_long):
    # Input: From Strava API Response. Starting latitude of segment, Starting longitude of segment
    # Output: Dictionary of Web Response for Segment Query. See top for example web response

    # Query construction using secret API Key
    url = 'http://api.wunderground.com/api/' + WU_API_KEY + '/geolookup/conditions/q/' \
          + str(user_lat) + ',' + str(user_long) + '.json'

    response_object = urlopen(url)
    json_string = response_object.read()
    dict_json = loads(json_string)

    wind_val = float(dict_json['current_observation']['wind_mph'])
    wind_dir = float(dict_json['current_observation']['wind_degrees'])

    wind_dict = {'wind mph': wind_val, 'wind direction': wind_dir}

    response_object.close()

    return wind_dict
