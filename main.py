from flask import Flask, render_template, request, flash, url_for, redirect
from get_wind_data import get_wind
from get_strava_segment import get_strava_data
from api_key_data import MY_STRAVA_PUBLIC_ACCESS_TOKEN
from calculate import *

app = Flask(__name__)

# Error handling

# Page not found
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', error=e)

# Method not found
@app.errorhandler(405)
def page_not_found(e):
    return render_template('405.html', error=e)

# Internal Server Error
@app.errorhandler(500)
def method_not_found(e):
    return render_template('500.html', error=e)

# Routing for homepage
@app.route('/')
def index():
    return render_template('index.html')

# Routing for strava segment windstat page
@app.route('/windstat/', methods=['POST'])
def windstat():
    error = ''
    try:
        if request.method == 'POST':
            # Receive data from form onb windstat. Getting users segment ID
            input_segment_id = request.form['segment_id']

            # do everything that needs to get done with user input here

            # Get strava data from user input in form of JSON. See get_strava_data for example JSON response.
            strava_data = get_strava_data(input_segment_id, MY_STRAVA_PUBLIC_ACCESS_TOKEN)

            # get wind data for start point (should be the same for the whole segment?)
            start_lat = strava_data['start_latitude']
            start_lng = strava_data['start_longitude']
            wind_dict = get_wind(start_lat, start_lng)

            # get angle difference
            angle_diff = wind_angle(bearing(strava_data['start_latitude'], strava_data['start_longitude'],
                                    strava_data['end_latitude'], strava_data['end_longitude']),
                                    wind_dict['wind direction'])

            # calculate headwind / tailwind component. Negative = headwind
            calculated_wind_assist = wind_assist(wind_dict['wind mph'], angle_diff)

            # calculate cross wind component (figure out what negative / positive mean)
            calculated_xwind = crosswind(wind_dict['wind mph'], angle_diff)

            # Store google map polyline data? or maybe pass it in (strava_data['polyline'])
            google_poly_line = strava_data['map']['polyline']



    except Exception as e:
        return render_template("/", error=error)

    # pass in data to be displayed on /windstat/result ('/windstat/result', data1, data2,....dataN)
    return redirect('/windstat/result',wind_dict, calculated_wind_assist, calculated_xwind, google_poly_line)

# TODO: CHECK ALL TYPES BEING PASSED. STRING -> INT / FLOAT NEEDS TO BE IMPLEMENTED IN MOST FUNCTIONS

# Check to make sure we only run the webserver when this file is run directly
if __name__ == "__main__":
    app.run(debug=True)