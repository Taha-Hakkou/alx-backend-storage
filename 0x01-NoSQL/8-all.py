#!/usr/bin/env python3
""" 8-all """
import pymongo


def list_all(mongo_collection):
    """ lists all documents in a collection """
    cursor = mongo_collection.find()
    if not cursor:
        return []
    return cursor
