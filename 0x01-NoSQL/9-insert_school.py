#!/usr/bin/env python3
""" 9-insert_school """
import pymongo


def insert_school(mongo_collection, **kwargs):
    """ inserts a new document in a collection based on kwargs """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
