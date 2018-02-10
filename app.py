"""
Main flask process
"""
from os import path, environ as env
import json
import atexit
from flask import Flask, request, jsonify
from bson import ObjectId
from pymongo import MongoClient

from models import get_type_latest, get_all_latest
from settings import load_env

load_env()

MC = MongoClient(env['MONGODB_URI'])
DIFF_NOTICES = 10

APP = Flask(__name__)

class JSONEncoder(json.JSONEncoder):
    """
    Class to convert ObjectId types to string
    """
    def default(self, o): # pylint: disable=E0202
        if isinstance(o, ObjectId):
            return str(o)
        elif isinstance(o, bytes):
            return o.decode("utf-8")
        return json.JSONEncoder.default(self, o)

@APP.route('/', methods=['GET'])
def index():
    """
    Handle http request to root
    """
    notices = get_all_latest()
    notices = JSONEncoder().encode(notices)
    return jsonify(Notices=json.loads(notices))

@APP.route('/<string:noticeboard>', methods=['GET'])
def get_type(noticeboard):
    """
    Handle http request for specific type
    """
    notices = get_type_latest(noticeboard)
    notices = JSONEncoder().encode(notices)
    return jsonify(Notices=json.loads(notices))

@APP.route('/diff/<string:noticeboard>', methods=['POST'])
def handle_notices_diff(noticeboard):
    """
    Method to check for new/updated notices
    """
    new_notices = []
    notices = request.get_json()
    section_coll = MC.get_database()[noticeboard]
    for notice in reversed(notices):
        db_notice = section_coll.find_one(notice)
        if db_notice is None:
            new_notices.append(notice)
            section_coll.insert_one(notice)
    new_notices = JSONEncoder().encode(new_notices)
    return jsonify(new_notices)

if __name__ == "__main__":
    APP.run(debug=True, host='0.0.0.0', port=5001, use_reloader=False)
