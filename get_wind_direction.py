#
# Filename: get_wind_direction.py
# Author: William Golembieski
# Initial Implementation: 09/21/2016
#
# Input:  Wind direction in degrees
# Output: Compass Heading


def get_wind_direction(direction):
    compass_headings = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW', 'N']
    return compass_headings[int(int(direction)/45)]