"""
Module to fetch data from the database
"""
from os import environ as env
from pymongo import MongoClient, DESCENDING

from settings import load_env

load_env()
MC = MongoClient(env['MONGODB_URI']).get_database()

def get_all_latest(notice_count=3):
    """
    Get latest notice_count notices from each noticeboard
    """
    latest = {}
    collections = MC.list_collection_names()
    for collection in collections:
        type_latest = get_type_latest(collection, notice_count)
        latest[collection] = type_latest
    return latest

def get_type_latest(notice_type, notice_count=3):
    """
    Get latest notice_count notices from notice_type
    """
    latest = []
    collections = MC.list_collection_names()
    if notice_type in collections:
        notices = MC[notice_type].find({}).sort('_id', DESCENDING).limit(notice_count)
        for notice in notices:
            latest.append(notice)
        return latest
    else:
        invalid_type = {
            "message": "The notice type you have requested is invalid"
        }
        return invalid_type

if __name__ == "__main__":
    get_all_latest()
