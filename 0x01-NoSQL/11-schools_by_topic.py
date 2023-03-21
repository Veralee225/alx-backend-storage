#!/usr/bin/env python3
""" a python module that returns the list of school having a specific topic"""
import pymongo



def schools_by_topic(mongo_collection, topic) -> list:
    """
    schools_by_topic - function that finds list of school
    Arguments:
        mongo_collection: the given mongo collection
        topic: the topic to be searched
    Returns:
        list of shool
    """
    output: list = []
    for dc in mongo_collection.find({"topics": topic}):
        output.append(dc)
    return output
