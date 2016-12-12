#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    calculate.py: Preforms bearing, wind angle, wind assist, and crosswind calculations.
    TODO: Wrap everything in ride class & rename to ride.py, because... OOP

    Initial Implementation: 09/06/2016 [William Golembieski]
    Last Modification: 12/11/2016 [William Golembieski]

"""

from math import cos, sin, atan2, degrees, radians

__author__ = "William Golembieski"
__email__ = "BillGolembieski@projectu23.com"


# def wind_direction(direction):
#     """
#     :param direction: Wind direction in degrees
#     :return: Cardinal direction representation for the wind. Note this is where the wind is coming FROM.
#     """
#
#     compass_headings = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW', 'N']
#
#     return compass_headings[int(int(direction)/45)]


def bearing(start_latitude, start_longitude, end_latitude, end_longitude):
    """
    :param start_latitude: Starting latitude in degrees (float)
    :param start_longitude: Starting longitude in degrees (float)
    :param end_latitude: Ending latitude in degrees (float)
    :param end_longitude: Ending longitude in degrees (float)
    :return: bearing of course in degrees using great-circle route from point A to point B (float)
    """

    # Convert input from degrees to radians so that sin() and cos() work properly. [degrees * (pi / 180)]
    start_lat = radians(start_latitude)
    start_long = radians(start_longitude)
    end_lat = radians(end_latitude)
    end_long = radians(end_longitude)

    # The formula gives the *initial* heading for a great-circle route from point A to point B
    # Source: http://mathforum.org/library/drmath/view/55417.html
    delta_long = end_long - start_long
    y = cos(end_lat) * sin(delta_long)
    x = cos(start_lat) * sin(end_lat) - sin(start_lat) * cos(end_lat) * cos(delta_long)
    bearing_rad = atan2(y, x)

    # Convert back to degrees && make sure returned bearing is positive if radians are negative
    # (ex. -1.0472 rad = -60 degrees = +300 degrees) [radians * (180 / pi)]
    bearing_deg = degrees(bearing_rad)
    bearing_deg = (bearing_deg + 360) % 360

    return bearing_deg


def wind_angle(travel_direction, wind_degrees):
    """
    :param travel_direction: travel direction in bearing degrees
    :param wind_degrees: wind direction in degrees. Note this is where the wind is coming FROM.
    :return: Angle difference between direction of travel and wind direction of travel
    """
    return travel_direction - ((wind_degrees + 180) % 360)


def wind_assist(wind_speed, angle):
    """
    :param wind_speed: wind speed in m/s or mph
    :param angle: Angle of wind from direction of travel
    :return: True wind assist in m/s or mph. Positive = Tailwind, Negative = Headwind, 0 = True Crosswind
    """
    return wind_speed * cos(radians(angle))


def crosswind(wind_speed, angle):
    """
    :param wind_speed: wind speed in m/s or mph
    :param angle: Angle of wind from direction of travel
    :return: Crosswind value. + or - values are returned to provide crosswind analysis. For now we abs() it in template.
    """
    return wind_speed * sin(radians(angle))

