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
@app.route('/windstat', methods=['POST'])
def windstat():
            # Receive data from form onb windstat. Getting users segment ID
            input_segment_id = request.form['segment_id']

            # Get strava data from user input in form of JSON. See get_strava_data for example JSON response.
            strava_data = get_strava_data(input_segment_id, MY_STRAVA_PUBLIC_ACCESS_TOKEN)

            # Start / End latitude longitude 'import' && cast as float
            start_lat = float(strava_data['start_latitude'])
            start_lng = float(strava_data['start_longitude'])
            end_lat = float(strava_data['end_latitude'])
            end_lng = float(strava_data['end_longitude'])

            google_poly_line = strava_data['map']['polyline']

            # get wind data for start point. // wind_dict = {'wind mph': wind_f, 'wind direction': wind_dir}
            wind_dict = get_wind(start_lat, start_lng)

            # get angle difference
            course_bearing = bearing(start_lat, start_lng, end_lat, end_lng)
            angle_diff = wind_angle(course_bearing, float(wind_dict['wind direction']))

            # calculate headwind / tailwind component. Negative = headwind
            calculated_wind_assist = wind_assist(float(wind_dict['wind mph']), angle_diff)

            # calculate cross wind component (figure out what negative / positive mean)
            calculated_xwind = crosswind(float(wind_dict['wind mph']), angle_diff)

    # pass in data to be displayed on /windstat/result ('/windstat/result', data1, data2,....dataN)
            return render_template('/windstat.html', wind_dict= wind_dict, calculated_wind_assist= calculated_wind_assist,
                                   calculated_xwind = calculated_xwind, google_poly_line = google_poly_line,
                                   strava_data = strava_data, input_segment_id = input_segment_id, angle_diff = angle_diff,
                                   course_bearing = course_bearing)


# Check to make sure we only run the webserver when this file is run directly
if __name__ == "__main__":
    app.run(debug=True)