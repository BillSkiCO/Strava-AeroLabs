#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    test_calculate.py: Run unit tests for calculate.py

    Initial Implementation: 12/13/2016 [William Golembieski]
    Last Modification: 12/13/2016 [William Golembieski]

"""

import calculate
import unittest


class TestCalculate(unittest.TestCase):

    def setUp(self):
        pass

    def test_bearing(self):
        """ def bearing(start_latitude, start_longitude, end_latitude, end_longitude):
        """
    # coordinates = []
    #
    # # Fill up a coordinates list
    # for latitude in range(-90, 90):
    #     for longitude in range(-180, 180):
    #         coordinates.append([latitude, longitude])

    # Each degree of latitude is approximately 69 miles (111 kilometers) apart.
    # Each minute (1/60th of a degree) is approximately one [nautical] mile
    # A degree of longitude is widest at the equator at 69.172 miles and gradually shrinks to zero at the poles
    # At 40° north or south the distance between a degree of longitude is 53 miles (85 km)

    # NW Quad: +Lat, -Long
    # NE Quad: +Lat, +Long
    # SW Quad: -Lat, -Long
    # SE Quad: -Lat, +Long
    # Lats: +- 90
    # Longs: +- 180

        # Check north bearing in all quadrants x == 0
        test_bearing_nw_quad = calculate.bearing(45.0, -90.0, 46.0, -90.0)
        self.assertTrue(self, test_bearing_nw_quad == 0, msg='calculate.bearing(NW Quad) not returning north')

        test_bearing_ne_quad = calculate.bearing(45.0, 90.0, 46.0, 90.0)
        self.assertTrue(self, test_bearing_ne_quad == 0, msg='calculate.bearing(NE Quad) not returning north')

        test_bearing_sw_quad = calculate.bearing(-45.0, -90.0, -44.0, -90.0)
        self.assertTrue(self, test_bearing_sw_quad == 0, msg='calculate.bearing(SW Quad) not returning north')

        test_bearing_se_quad = calculate.bearing(-45.0, 90.0, -44.0, 90.0)
        self.assertTrue(self, test_bearing_se_quad == 0, msg='calculate.bearing(SE Quad) not returning north')

        # Check northeast bearing 0 < x < 90
        # Check east bearing x == 90
        # Check southeast bearing 90 < x < 180
        # Check south bearing x == 180
        # Check southwest bearing 180 < x < 270
        # Check west bearing x == 270
        # Check northwest bearing 270 < x < 360


if __name__ == '__main__':
    unittest.main()