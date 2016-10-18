#!/usr/bin/env python

"""
    calculate.py: Preforms bearing, wind angle, wind assist, and crosswind calculations

    Initial Implementation: 09/06/2016 [William Golembieski]
    Last Modification: 10/17/2016 [William Golembieski]

"""

from math import cos, sin, atan2, degrees, radians

__author__ = "William Golembieski"
__copyright__ = "Copyright 2016, Strava AeroLabs"
__credits__ = ["William Golembieski"]
__license__ = "GNU General Public License v3.0"
__version__ = "1.0.0"
__maintainer__ = "William Golembieski"
__email__ = "BillGolembieski@projectu23.com"
__status__ = "Production"


# def wind_direction(direction):
#     # Input: Wind direction in degrees
#     # Output: Cardinal direction representation for the wind
#     compass_headings = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW', 'N']
#
#     return compass_headings[int(int(direction)/45)]


def bearing(start_latitude, start_longitude, end_latitude, end_longitude):
    # Input: (all floats)Starting latitude, starting longitude, ending latitude, ending longitude
    # Output: (float)Bearing in degrees, from start point to end point

    # Convert input from degrees to radians so that sin and cos work properly
    start_lat = radians(start_latitude)
    start_long = radians(start_longitude)
    end_lat = radians(end_latitude)
    end_long = radians(end_longitude)
    delta_long = end_long - start_long

    # The formula gives the *initial* heading for a great-circle route from point A to point B
    # Source: http://mathforum.org/library/drmath/view/55417.html
    y = cos(end_lat) * sin(delta_long)
    x = cos(start_lat) * sin(end_lat) - sin(start_lat) * cos(end_lat) * cos(delta_long)
    bearing_rad = atan2(y, x)

    bearing_deg = degrees(bearing_rad)
    bearing_deg = (bearing_deg + 360) % 360

    return bearing_deg


def wind_angle(travel_direction, wind_degrees):
    # Input: Travel Direction in bearing degrees, wind direction in degrees. Note this is where the wind is coming FROM.
    # Output: Angle difference between direction of travel and wind direction of travel
    return travel_direction - ((wind_degrees + 180) % 360)


def wind_assist(wind_speed, angle):
    # Input: Wind Speed in m/s or mph, Angle of wind from direction of travel
    # Output: True wind assist in m/s or mph. Positive = Tailwind, Negative = Headwind, 0 = True Crosswind
    return wind_speed * cos(radians(angle))


def crosswind(wind_speed, angle):
    # Input: Wind Speed in m/s or mph, Angle of wind from direction of travel
    # Output: Crosswind value
    return wind_speed * sin(radians(angle))

