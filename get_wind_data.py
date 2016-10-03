#
# Filename: get_wind_data.py
# Author: William Golembieski
# Initial Implementation: 09/06/2016
#
# API Call to Weather Underground to get wind data.
#

import urllib2
import json

from api_key_data import WU_API_KEY

def get_wind(user_lat, user_long):
    # Query construction using secret API Key
    url = 'http://api.wunderground.com/api/' + WU_API_KEY + '/geolookup/conditions/q/' \
          + str(user_lat) + ',' + str(user_long) + '.json'

    response_object = urllib2.urlopen(url)
    json_string = response_object.read()
    dict_json = json.loads(json_string)

    wind_f = float(dict_json['current_observation']['wind_mph'])
    wind_dir = float(dict_json['current_observation']['wind_degrees'])

    print dict_json

    wind_dict = {'wind mph': wind_f, 'wind direction': wind_dir}

    response_object.close()

    return wind_dict
