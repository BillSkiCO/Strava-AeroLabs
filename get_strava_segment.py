#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    get_strava_segment.py: API call to strava to get segment details

    Example web response for https://www.strava.com/api/v3/segments/660072?access_token=YOUR_PUB_ACCESS_TOKEN

    {"id":660072,"resource_state":3,"name":"Grefsenkollen","activity_type":"Ride","distance":1827.31,
    "average_grade":6.7,"maximum_grade":13.1,"elevation_high":371.8,"elevation_low":249.6,
    "start_latlng":[59.958640951663256,10.798284988850355],"end_latlng":[59.95867892168462,10.804210994392633],
    "start_latitude":59.958640951663256,"start_longitude":10.798284988850355,
    "end_latitude":59.95867892168462,"end_longitude":10.804210994392633,
    "climb_category":1,"city":null,"state":"Oslo","country":"Norway","private":false,"hazardous":false,
    "starred":false,"created_at":"2011-05-31T14:42:32Z","updated_at":"2016-09-21T08:03:21Z",
    "total_elevation_gain":122.2,
    "map":{"id":"s660072","polyline":"ot}lJg`|`A}@AiBIe@?gADo@AUIUMkAuAmAgAw@i@{BkAe@]OSq@wAWYSG[Be@X{@t@OHS?
    GCQMU_@Mm@Eu@DkAH[Rc@TSbA_@PKNOZo@p@wBV]XQPEtAKr@CZ?NDXPLPRv@h@zCh@zBRf@V^b@^n@RtALj@@XEdGwB`@]NSX{@Ha@RmBZ_EDaBCoAIa
    @EOQQICI?[PW^]`A_@tAONG?ICGIOk@Ko@", "resource_state":3},
    "effort_count":91193,"athlete_count":5754,"star_count":1079,
    "athlete_segment_stats":{"pr_elapsed_time":null,"pr_date":null,"effort_count":0}}

    Initial Implementation: 09/06/2016 [William Golembieski]
    Last Modification: 12/11/2016 [William Golembieski]

"""

from flask import render_template
from urllib2 import urlopen, HTTPError
from json import loads

__author__ = "William Golembieski"
__email__ = "BillGolembieski@projectu23.com"


def get_strava_data(segment_url, public_access_token):
    """
    :param segment_url:  Strava URL containing segment ID at the end example 'https://www.strava.com/segments/613' \
                         will still work as long as last number is segment ID
    :param public_access_token: A public access token for the app
    :return: Dictionary of Web Response for Segment Query. See top for example web response
    """

    seg_id = segment_url.split('/')
    url = 'https://www.strava.com/api/v3/segments/' + str(seg_id[-1]) + '/?access_token=' + str(public_access_token)
    try:
        # Call to urllib2.urlopen()
        response_object = urlopen(url)

    # Call to urllib2.HTTPError() in the case that strava url does not exist
    except HTTPError as e:
        render_template('/strava404.html/', error=e)

    json_string = response_object.read()

    # Call to json.loads
    dict_json = loads(json_string)

    response_object.close()

    return dict_json