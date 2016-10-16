from flask import Flask, render_template, request, flash, url_for, redirect, jsonify
import datetime
from get_wind_data import get_wind
from get_strava_segment import get_strava_data
from api_key_data import MY_STRAVA_PUBLIC_ACCESS_TOKEN, GOOGLE_API_KEY
from calculate import *
import polyline

app = Flask(__name__)

# Error handling

# Page not found
@app.errorhandler(404)
def page_not_found(e):
    return render_template('405.html', error=e)

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
            input_segment_url = request.form['segment_url']

            # Get strava data from user input in form of JSON. See get_strava_data for example JSON response.
            strava_data = get_strava_data(input_segment_url, MY_STRAVA_PUBLIC_ACCESS_TOKEN)

            # Start / End latitude longitude 'import' && cast as float
            start_lat = float(strava_data['start_latitude'])
            start_lng = float(strava_data['start_longitude'])
            end_lat = float(strava_data['end_latitude'])
            end_lng = float(strava_data['end_longitude'])

            center_lat = start_lat - ((start_lat - end_lat)/2)
            center_lng = start_lng - ((start_lng - end_lng)/2)

            google_poly_line = strava_data['map']['polyline']
            dict_lat_lng = polyline.decode(strava_data['map']['polyline'])
            google_img_url = \
                'http://maps.googleapis.com/maps/api/staticmap?sensor=false&key='+ GOOGLE_API_KEY + \
                '&size=300x300&path=weight:3|color:red|enc:'+ google_poly_line
            print google_img_url

            # get wind data for start point. // wind_dict = {'wind mph': wind_f, 'wind direction': wind_dir}
            wind_dict = get_wind(start_lat, start_lng)
            wind_speed_mph = wind_dict['wind mph']
            wind_dir = float(wind_dict['wind direction']) # Account for arrow in /static/images @ 45 deg

            # get angle difference
            course_bearing = bearing(start_lat, start_lng, end_lat, end_lng)
            angle_diff = wind_angle(course_bearing, float(wind_dict['wind direction']))

            # calculate headwind / tailwind component. Negative = headwind
            calculated_wind_assist = wind_assist(float(wind_dict['wind mph']), angle_diff)

            if calculated_wind_assist > 0:
                    wind_class = "Tailwind"
            else:
                    wind_class = "Headwind"

            # enumerate intensity of headwind / tailwind

            if calculated_wind_assist > 5.0:
                # Strong Tailwind
                assist_enum = 1
            elif 5.0 > calculated_wind_assist >= 0:
                # Moderate Tailwind
                assist_enum = 2
            elif 0 > calculated_wind_assist > -5.0:
                # Moderate Headwind
                assist_enum = 3
            else:
                # Strong Headwind
                assist_enum = 4

            # calculate cross wind component (figure out what negative / positive mean)
            calculated_xwind = crosswind(float(wind_dict['wind mph']), angle_diff)

    # pass in data to be displayed on /windstat/result ('/windstat/result', data1, data2,....dataN)
            return render_template('/windstat.html', wind_dict= wind_dict, calculated_wind_assist= abs(calculated_wind_assist),
                                   calculated_xwind = abs(calculated_xwind), google_poly_line = google_poly_line,
                                   strava_data = strava_data, input_segment_id = input_segment_url, angle_diff = angle_diff,
                                   course_bearing = int(course_bearing), center_lat = center_lat, center_lng = center_lng,
                                   dict_lat_lng = dict_lat_lng, google_img_url = google_img_url,
                                   wind_dir_deg = int(wind_dir), wind_class = wind_class, wind_speed_mph = wind_speed_mph,
                                   assist_enum = assist_enum)


# Check to make sure we only run the webserver when this file is run directly
if __name__ == "__main__":
    app.run(debug=True)