#!/usr/bin/python3
"""hbnb filters"""


from flask import Flask, render_template
from models import storage
from models import *
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Filter like 6-index"""
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown_db(text):
    """Close"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
