# API call to strava to get segment details
#
# Example web response for https://www.strava.com/api/v3/segments/660072?access_token=YOUR_PUB_ACCESS_TOKEN
#
# {"id":660072,"resource_state":3,"name":"Grefsenkollen","activity_type":"Ride","distance":1827.31,
# "average_grade":6.7,"maximum_grade":13.1,"elevation_high":371.8,"elevation_low":249.6,
# "start_latlng":[59.958640951663256,10.798284988850355],"end_latlng":[59.95867892168462,10.804210994392633],
# "start_latitude":59.958640951663256,"start_longitude":10.798284988850355,
# "end_latitude":59.95867892168462,"end_longitude":10.804210994392633,
# "climb_category":1,"city":null,"state":"Oslo","country":"Norway","private":false,"hazardous":false,
# "starred":false,"created_at":"2011-05-31T14:42:32Z","updated_at":"2016-09-21T08:03:21Z",
# "total_elevation_gain":122.2,
# "map":{"id":"s660072","polyline":"ot}lJg`|`A}@AiBIe@?gADo@AUIUMkAuAmAgAw@i@{BkAe@]OSq@wAWYSG[Be@X{@t@OHS?
# GCQMU_@Mm@Eu@DkAH[Rc@TSbA_@PKNOZo@p@wBV]XQPEtAKr@CZ?NDXPLPRv@h@zCh@zBRf@V^b@^n@RtALj@@XEdGwB`@]NSX{@Ha@RmBZ_EDaBCoAIa
# @EOQQICI?[PW^]`A_@tAONG?ICGIOk@Ko@", "resource_state":3},
# "effort_count":91193,"athlete_count":5754,"star_count":1079,
# "athlete_segment_stats":{"pr_elapsed_time":null,"pr_date":null,"effort_count":0}}


import urllib2
import json

def get_strava_data(segment_id, public_access_token):
    # Query to get strava segment data
    # Input: Segment ID, Strava App Public Access Token
    # Output: Dictionary of Web Response for Segment Query. See top for example web response
    url = 'https://www.strava.com/api/v3/segments/'+ segment_id + '/?access_token=' + public_access_token

    response_object = urllib2.urlopen(url)
    json_string = response_object.read()
    dict_json = json.loads(json_string)

    response_object.close()

    return dict_json