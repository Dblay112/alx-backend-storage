#!/usr/bin/env python3
"""interpreter used"""


def schools_by_topic(mongo_collection, topic):
    """
    a Python function that returns
    the list of school having a specific topic
    Args:
    mongo_collection:collection object
    topic: string(topic) to be searched
    returns:
    topic(string) to be searched
    """
    return mongo_collection.find({"topics": topic})
