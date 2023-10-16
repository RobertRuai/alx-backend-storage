#!/usr/bin/env python3
"""schools_by_topic omdule"""


def schools_by_topic(mongo_collection, topic):
    """returns list of school having a specific topic"""
    res = mongo_collection.find({"topics": topic})
    return res
