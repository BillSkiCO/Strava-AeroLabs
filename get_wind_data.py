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

def get_wind(user_city, user_state):
    # Query construction using secret API Key
    url = 'http://api.wunderground.com/api/' + WU_API_KEY + '/geolookup/conditions/q/' \
          + user_state + '/' + user_city + '.json'

    response_object = urllib2.urlopen(url)
    json_string = response_object.read()
    dict_json = json.loads(json_string)

    location = dict_json['location']['city']
    wind_f = dict_json['current_observation']['wind_mph']

    response_object.close()

    return "Current wind is: %s mph in %s, %s" % (wind_f, location, user_state)