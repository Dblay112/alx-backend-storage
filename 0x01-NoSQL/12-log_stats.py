#!/usr/bin/env python3
"""interpreter used"""

from pymongo import MongoClient


def logs_count(mongo_collection):
    """
    Function that returns the number of logs in the collection.
    """
    return mongo_collection.count_documents({})


def method_count(mongo_collection, method):
    """
    Function that returns the count of logs with a specific HTTP method.
    """
    return mongo_collection.count_documents({"method": method})


def path_count(mongo_collection, method, path):
    """
    Function that returns the number of logs with a specific HTTP method and path.
    """
    return mongo_collection.count_documents({"method": method, "path": path})


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx

    print("{} logs".format(logs_count(nginx)))
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print("\tmethod {}: {}".format(method, method_count(nginx, method)))

    print("{} status check".format(path_count(nginx, "GET", "/status")))
