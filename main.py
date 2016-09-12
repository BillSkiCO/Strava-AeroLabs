from flask import Flask, render_template, request, flash, url_for, redirect
from get_wind_data import get_wind

app = Flask(__name__)

# Error handling

# Page not found
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', error = e)

# Method not found
@app.errorhandler(405)
def page_not_found(e):
    return render_template('405.html', error = e)

# Internal Server Error
@app.errorhandler(500)
def method_not_found(e):
    return render_template('500.html', error = e)

#routing tying a URL to a python function
@app.route('/', methods=['GET', 'POST'])
def index():
    error = ''
    try:
        if request.method == 'POST':
            attempted_segment_id = request.form['segment_id']

            if attempted_segment_id == '123456789':
                return redirect(url_for('/'))
            else:
                error = 'Invalid Strava Segment ID. Try Again'

    except Exception as e:
        return render_template("/", error=error)



    return render_template('index.html')


# Check to make sure we only run the webserver when this file is run directly
if __name__ == "__main__":
    app.run(debug=True)