#!/usr/bin/env python3
"""location of interpreter"""


def insert_school(mongo_collection, **kwargs):
    """
    function that inserts a new document in a collection based on kwargs

    Returns:
    the new _id
    """
    new_doc_id = mongo_collection.insert_one(kwargs).inserted_id
    return new_doc_id
