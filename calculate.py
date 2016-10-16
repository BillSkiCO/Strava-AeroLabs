#
# Filename: calculate.py
# Author: William Golembieski
# Initial Implementation: 09/23/2016
#
# Calculations for wind direction, bearing, wind angle, wind assistance, and crosswind
#

from math import cos, sin, atan2, degrees, radians


def wind_direction(direction):
    # Input: Wind direction in degrees
    # Output: Cardinal direction representation for the wind
    compass_headings = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW', 'N']

    return compass_headings[int(int(direction)/45)]


def bearing(start_lat, start_lng, end_lat, end_lng):
    # Input: (all floats)Starting latitude, starting longitude, ending latitude, ending longitude
    # Output: (float)Bearing direction in degrees, from start point to end point
    y = cos(end_lat) * sin(end_lng - start_lng)
    x = cos(start_lat) * sin(end_lat) - sin(start_lat) * cos(end_lat) * cos(end_lng - start_lng)

    bearing_rad = atan2(y, x)
    bearing_deg = degrees(bearing_rad)
    bearing_deg = (bearing_deg + 360) % 360
    bearing_deg = (bearing_deg + 180) % 360

    return bearing_deg


def wind_angle(travel_direction, wind_degrees):
    # Input: Travel Direction in bearing degrees, wind direction in degrees. Note this is where the wind is coming FROM.
    # Output: Angle difference between direction of travel and wind direction of travel
    return travel_direction - ((wind_degrees + 180) % 360)


def wind_assist(wind_speed, wind_angle):
    # Input: Wind Speed in m/s or mph, Angle of wind from direction of travel
    # Output: True wind assist in m/s or mph. Positive = Tailwind, Negative = Headwind, 0 = True Crosswind
    return wind_speed * cos(radians(wind_angle))


def crosswind(wind_speed, wind_angle):
    # Input: Wind Speed in m/s or mph, Angle of wind from direction of travel
    # Output: Crosswind value
    return wind_speed * sin(radians(wind_angle))

