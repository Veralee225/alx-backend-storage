#!/usr/bin/env python3
""" a python module to list all documents in a collection"""
import pymongo


def list_all(mongo_collection) -> list:
    """
    list_all: funcion to list all documents
    Arguments:
        mongo_collection: the given mongo collection
    Returns:
        all documents in a mongo collection
    """
    doc: list = []
    for d in mongo_collection.find():
        doc.append(d)
    return (doc)
