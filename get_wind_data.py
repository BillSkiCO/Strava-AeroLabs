#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    get_wind_data.py: using strava start and end latitude / longitude, output wind speed in mph and wind direction
                      in degrees from nearest weather underground station.

    Initial Implementation: 09/06/2016 [William Golembieski]
    Last Modification: 12/11/2016 [William Golembieski]

"""

from flask import render_template
from urllib2 import urlopen, HTTPError
from json import loads
from config import WU_API_KEY

__author__ = "William Golembieski"
__email__ = "BillGolembieski@projectu23.com"


def get_wind(user_lat, user_long):
    """
    :param user_lat: Starting latitude of segment in degrees (float)
    :param user_long: Starting longitude of segment in degrees (float)
    :return: Dictionary of Web response for segment query. (dict in JSON format SOOPA FAST)
    """

    url = 'http://api.wunderground.com/api/' + WU_API_KEY + '/geolookup/conditions/q/' \
          + str(user_lat) + ',' + str(user_long) + '.json'

    # Call to urllib2.urlopen()
    try:
        response_object = urlopen(url)
    # Call to urllib2.HTTPError() in event the url does not work
    except HTTPError, e:
        return render_template('wundererror.html', error=e)

    json_string = response_object.read()

    # Call to json.loads()
    dict_json = loads(json_string)

    # Objects stored in dict_json are all of type str due to read() *see documentation*.
    # Float conversion for calculation.
    wind_val = float(dict_json['current_observation']['wind_mph'])
    wind_dir = float(dict_json['current_observation']['wind_degrees'])

    # Hash wind_val and wind_dir using dictionary data structure
    wind_dict = {'wind mph': wind_val, 'wind direction': wind_dir}

    response_object.close()

    return wind_dict
