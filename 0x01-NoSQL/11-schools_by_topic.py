#!/usr/bin/env python3
"""return a doc list"""


def schools_by_topic(mongo_collection, topic):
    """get schools by topic"""
    return  mongo_collection.find({"topics": {"$in": [topic]}})
