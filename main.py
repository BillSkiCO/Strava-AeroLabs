from flask import Flask, render_template, request, flash, url_for, redirect
from get_wind_data import get_wind
from get_strava_segment import get_strava_data
from api_key_data import MY_STRAVA_PUBLIC_ACCESS_TOKEN

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
            input_segment_id = request.form['segment_id']
            strava_data = get_strava_data(input_segment_id, MY_STRAVA_PUBLIC_ACCESS_TOKEN)

    except Exception as e:
        return render_template("/", error=error)

    # CODE TO COMPUTE TAILWIND
    # attempted_segment_id is user input

    return render_template('segment_form_action.html, ')










# Check to make sure we only run the webserver when this file is run directly
if __name__ == "__main__":
    app.run(debug=True)