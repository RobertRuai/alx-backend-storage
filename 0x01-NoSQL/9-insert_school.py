#!/usr/bin/env python3
"""insert_school module"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection"""
    res = mongo_collection.insert_one(kwargs)
    return res.inserted_id
