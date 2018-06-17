# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import logging
import json
from flask import Flask, render_template, request, jsonify, make_response

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')


def get_latlng(url):
    """parses the google maps url to get the latitude and longitude data"""
    lat_lng_data = url.split('@')[1].split('/data')[0]
    lat, lng, zoom = lat_lng_data.split(',')
    return (lat, lng, zoom)

def add_latlng(data):
    results = []

    for item in data:
        lat, lng, zoom = get_latlng(item['google_maps_url'])
        item['lat'] = float(lat)
        item['lng'] = float(lng)
        results.append(item)

    return results

def get_data():
    PROJECT_DIR = os.path.dirname(__file__)
    data = json.loads(open(os.path.join(PROJECT_DIR, 'static/sample_data.json')).read())
    return data

@app.route('/api/v1/properties/get')
def get_properties():
    data = get_data()
    response = add_latlng(data)
    r = make_response(jsonify(data))
    r.headers.set('Access-Control-Allow-Origin', "*")
    return r


@app.route('/')
def home():
    data = get_data()
    response = add_latlng(data)
    return render_template('index.html', data=response)

