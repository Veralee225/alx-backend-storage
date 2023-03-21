#!/usr/bin/env python3
""" a python module to change all topics of a school document"""
import pymongo



def update_topics(mongo_collection, name, topics):
    """
    update_topics - function to update topicsof a school
    Arguments:
        mongo_collection: the given mongo collection
        name: the school name to be updated
        topics: list of topics
    Returns:
        nothing
    """
    rqrd_attr = {"name": name}
    updt_attr = {"$set": {"topics": topics}}
    mongo_collection.update_many(rqrd_attr, updt_attr)
