#!/usr/bin/env python3
""" 101-students """
import pymongo


def top_students(mongo_collection):
    """ returns all students sorted by average score """
    return mongo_collection.aggregate([
        { '$addFields':
            { 'averageScore':
                { '$avg': '$topics.score' }
            }
        },
        { '$sort':
            { 'averageScore': pymongo.DESCENDING }
        }
    ])
