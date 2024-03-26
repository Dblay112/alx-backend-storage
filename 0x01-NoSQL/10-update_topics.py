#!/usr/bin/env python3
"""interpreter used"""


def update_topics(mongo_collection, name, topics):
    """
    Updates topics of all school documents with the given name.

    Args:
        mongo_collection: The pymongo collection object.
        name (str): School name to update.
        topics (list of str): List of topics.
    """
    filter = {"name": name}
    update = {"$set": {"topics": topics}}
    return mongo_collection.update_many(filter, update)
