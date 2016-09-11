from flask import Flask, render_template
from get_wind_data import get_wind

app = Flask(__name__, static_folder="X:/AeroLabs/Strava-AeroLabs/static")

#routing tying a URL to a python function
@app.route('/')
def index():
    return render_template('index.html')
    #return get_wind('Cicero', 'NY')

# Check to make sure we only run the webserver when this file is run directly
if __name__ == "__main__":
    app.run(debug=True)