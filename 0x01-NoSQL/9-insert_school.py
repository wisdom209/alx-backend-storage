#!/usr/bin/env python3
"""pymongo script"""


def insert_school(mongo_collection, **kwargs):
    """insert an item"""
    doc = mongo_collection.insert_one(kwargs)
    return doc.inserted_id
