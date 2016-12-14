#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    test_calculate.py: Run unit tests for calculate.py

    Initial Implementation: 12/13/2016 [William Golembieski]
    Last Modification: 12/14/2016 [William Golembieski]

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
        test_bearing_nw_quad_is_north = calculate.bearing(45.0, -90.0, 46.0, -90.0)
        self.assertTrue(test_bearing_nw_quad_is_north == 0,
                        msg='calculate.bearing(NW Quad) not returning north: '
                        + str(test_bearing_nw_quad_is_north))

        test_bearing_ne_quad_is_north = calculate.bearing(45.0, 90.0, 46.0, 90.0)
        self.assertTrue(test_bearing_ne_quad_is_north == 0,
                        msg='calculate.bearing(NE Quad) not returning north: '
                        + str(test_bearing_ne_quad_is_north))

        test_bearing_sw_quad_is_north = calculate.bearing(-45.0, -90.0, -44.0, -90.0)
        self.assertTrue(test_bearing_sw_quad_is_north == 0,
                        msg='calculate.bearing(SW Quad) not returning north: '
                        + str(test_bearing_sw_quad_is_north))

        test_bearing_se_quad_is_north = calculate.bearing(-45.0, 90.0, -44.0, 90.0)
        self.assertTrue(test_bearing_se_quad_is_north == 0,
                        msg='calculate.bearing(SE Quad) not returning north: '
                        + str(test_bearing_se_quad_is_north))

        # Check northeast bearing 0 < x < 90
        test_bearing_nw_quad_is_northeast = calculate.bearing(45.0, -90.0, 46.0, -89.0)
        self.assertTrue(0 < test_bearing_nw_quad_is_northeast < 90,
                        msg='calculate.bearing(NW Quad) not returning northeast: '
                        + str(test_bearing_nw_quad_is_northeast))

        test_bearing_ne_quad_is_northeast = calculate.bearing(45.0, 90.0, 46.0, 91.0)
        self.assertTrue(0 < test_bearing_ne_quad_is_northeast < 90,
                        msg='calculate.bearing(NE Quad) not returning northeast: '
                        + str(test_bearing_ne_quad_is_northeast))

        test_bearing_sw_quad_is_northeast = calculate.bearing(-45.0, -90.0, -44.0, -89.0)
        self.assertTrue(0 < test_bearing_sw_quad_is_northeast < 90,
                        msg='calculate.bearing(SW Quad) not returning northeast: '
                        + str(test_bearing_sw_quad_is_northeast))

        test_bearing_se_quad_is_northeast = calculate.bearing(-45.0, 90.0, -44.0, 91.0)
        self.assertTrue(0 < test_bearing_se_quad_is_northeast < 90,
                        msg='calculate.bearing(SE Quad) not returning northeast: '
                        + str(test_bearing_se_quad_is_northeast))

        # Check east bearing x about == 90
        test_bearing_nw_quad_is_east = calculate.bearing(45.0, -90.0, 45.0, -89.0)
        self.assertTrue(89 < test_bearing_nw_quad_is_east < 91,
                        msg='calculate.bearing(NW Quad) not returning east: '
                        + str(test_bearing_nw_quad_is_east))

        test_bearing_ne_quad_is_east = calculate.bearing(45.0, 90.0, 45.0, 91.0)
        self.assertTrue(89 < test_bearing_ne_quad_is_east < 91,
                        msg='calculate.bearing(NE Quad) not returning east: '
                        + str(test_bearing_ne_quad_is_east))

        test_bearing_sw_quad_is_east = calculate.bearing(-45.0, -90.0, -45.0, -89.0)
        self.assertTrue(89 < test_bearing_sw_quad_is_east < 91,
                        msg='calculate.bearing(SW Quad) not returning east: '
                        + str(test_bearing_sw_quad_is_east))

        test_bearing_se_quad_is_east = calculate.bearing(-45.0, 90.0, -45.0, 91.0)
        self.assertTrue(89 < test_bearing_se_quad_is_east < 91,
                        msg='calculate.bearing(SE Quad) not returning east: '
                        + str(test_bearing_se_quad_is_east))

        # Check southeast bearing 90 < x < 180
        test_bearing_nw_quad_is_southeast = calculate.bearing(45.0, -90.0, 44.0, -89.0)
        self.assertTrue(90 < test_bearing_nw_quad_is_southeast < 180,
                        msg='calculate.bearing(NW Quad) not returning southeast: '
                        + str(test_bearing_nw_quad_is_southeast))

        test_bearing_ne_quad_is_southeast = calculate.bearing(45.0, 90.0, 44.0, 91.0)
        self.assertTrue(90 < test_bearing_ne_quad_is_southeast < 180,
                        msg='calculate.bearing(NE Quad) not returning southeast: '
                        + str(test_bearing_ne_quad_is_southeast))

        test_bearing_sw_quad_is_southeast = calculate.bearing(-45.0, -90.0, -46.0, -89.0)
        self.assertTrue(90 < test_bearing_sw_quad_is_southeast < 180,
                        msg='calculate.bearing(SW Quad) not returning southeast: '
                        + str(test_bearing_sw_quad_is_southeast))

        test_bearing_se_quad_is_southeast = calculate.bearing(-45.0, 90.0, -46.0, 91.0)
        self.assertTrue(90 < test_bearing_se_quad_is_southeast < 180,
                        msg='calculate.bearing(SE Quad) not returning southeast: '
                        + str(test_bearing_se_quad_is_southeast))

        # Check south bearing x == 180
        test_bearing_nw_quad_is_south = calculate.bearing(45.0, -90.0, 44.0, -90.0)
        self.assertTrue(179 < test_bearing_nw_quad_is_south < 181,
                        msg='calculate.bearing(NW Quad) not returning south: '
                        + str(test_bearing_nw_quad_is_south))

        test_bearing_ne_quad_is_south = calculate.bearing(45.0, 90.0, 44.0, 90.0)
        self.assertTrue(179 < test_bearing_ne_quad_is_south < 181,
                        msg='calculate.bearing(NE Quad) not returning south: '
                        + str(test_bearing_ne_quad_is_south))

        test_bearing_sw_quad_is_south = calculate.bearing(-45.0, -90.0, -46.0, -90.0)
        self.assertTrue(179 < test_bearing_sw_quad_is_south < 181,
                        msg='calculate.bearing(SW Quad) not returning south: '
                        + str(test_bearing_sw_quad_is_south))

        test_bearing_se_quad_is_north = calculate.bearing(-45.0, 90.0, -46.0, 90.0)
        self.assertTrue(179 < test_bearing_se_quad_is_north < 181,
                        msg='calculate.bearing(SE Quad) not returning south: '
                        + str(test_bearing_se_quad_is_north))

        # Check southwest bearing 180 < x < 270
        test_bearing_nw_quad_is_southwest = calculate.bearing(45.0, -90.0, 44.0, -91.0)
        self.assertTrue(180 < test_bearing_nw_quad_is_southwest < 270,
                        msg='calculate.bearing(NW Quad) not returning southwest: '
                        + str(test_bearing_nw_quad_is_southwest))

        test_bearing_ne_quad_is_southwest = calculate.bearing(45.0, 90.0, 44.0, 89.0)
        self.assertTrue(180 < test_bearing_ne_quad_is_southwest < 270,
                        msg='calculate.bearing(NE Quad) not returning southwest: '
                        + str(test_bearing_ne_quad_is_southwest))

        test_bearing_sw_quad_is_southwest = calculate.bearing(-45.0, -90.0, -46.0, -91.0)
        self.assertTrue(180 < test_bearing_sw_quad_is_southwest < 270,
                        msg='calculate.bearing(SW Quad) not returning southwest: '
                        + str(test_bearing_sw_quad_is_southwest))

        test_bearing_se_quad_is_southwest = calculate.bearing(-45.0, 90.0, -46.0, 89.0)
        self.assertTrue(180 < test_bearing_se_quad_is_southwest < 270,
                        msg='calculate.bearing(SE Quad) not returning southwest: '
                        + str(test_bearing_se_quad_is_southwest))

        # Check west bearing about == 270
        test_bearing_nw_quad_is_west = calculate.bearing(45.0, -90.0, 45.0, -91.0)
        self.assertTrue(269 < test_bearing_nw_quad_is_west < 271,
                        msg='calculate.bearing(NW Quad) not returning west: '
                        + str(test_bearing_nw_quad_is_west))

        test_bearing_ne_quad_is_west = calculate.bearing(45.0, 90.0, 45.0, 89.0)
        self.assertTrue(269 < test_bearing_ne_quad_is_west < 271,
                        msg='calculate.bearing(NE Quad) not returning west: '
                        + str(test_bearing_ne_quad_is_west))

        test_bearing_sw_quad_is_west = calculate.bearing(-45.0, -90.0, -45.0, -91.0)
        self.assertTrue(269 < test_bearing_sw_quad_is_west < 271,
                        msg='calculate.bearing(SW Quad) not returning west: '
                        + str(test_bearing_sw_quad_is_west))

        test_bearing_se_quad_is_west = calculate.bearing(-45.0, 90.0, -45.0, 89.0)
        self.assertTrue(269 < test_bearing_se_quad_is_west < 271,
                        msg='calculate.bearing(SE Quad) not returning west: '
                        + str(test_bearing_se_quad_is_west))

        # Check northwest bearing 270 < x < 360
        test_bearing_nw_quad_is_northwest = calculate.bearing(45.0, -90.0, 46.0, -91.0)
        self.assertTrue(270 < test_bearing_nw_quad_is_northwest < 360,
                        msg='calculate.bearing(NW Quad) not returning northwest: '
                        + str(test_bearing_nw_quad_is_northwest))

        test_bearing_ne_quad_is_northwest = calculate.bearing(45.0, 90.0, 46.0, 89.0)
        self.assertTrue(270 < test_bearing_ne_quad_is_northwest < 360,
                        msg='calculate.bearing(NE Quad) not returning northwest: '
                        + str(test_bearing_ne_quad_is_northwest))

        test_bearing_sw_quad_is_northwest = calculate.bearing(-45.0, -90.0, -44.0, -91.0)
        self.assertTrue(270 < test_bearing_sw_quad_is_northwest < 360,
                        msg='calculate.bearing(SW Quad) not returning northwest: '
                        + str(test_bearing_sw_quad_is_northwest))

        test_bearing_se_quad_is_northwest = calculate.bearing(-45.0, 90.0, -44.0, 89.0)
        self.assertTrue(270 < test_bearing_se_quad_is_northwest < 360,
                        msg='calculate.bearing(SE Quad) not returning northwest: '
                            + str(test_bearing_se_quad_is_northwest))


if __name__ == '__main__':
    unittest.main()