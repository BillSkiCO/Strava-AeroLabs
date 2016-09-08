from flask import Flask
from get_wind_data import *

app = Flask(__name__)

#routing tying a URL to a python function
@app.route('/')
def index():
    return get_wind('Cicero', 'NY')

# Check to make sure we only run the webserver when this file is run directly
if __name__ == "__main__":
    app.run(debug=True)