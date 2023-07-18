#!/usr/bin/env python3
"""Pymongo script"""
from pymongo import MongoClient
client = MongoClient()
db = client.my_db


def list_all(mongo_collection):
    """list all documents in a collection"""
    return mongo_collection.find()
