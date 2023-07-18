#!/usr/bin/python3


def schools_by_topic(mongo_collection, topic):
    """get schools by topic"""
    docs =  mongo_collection.find({"topic": topic})
    doclist = [doc for doc in docs]
    return doclist
