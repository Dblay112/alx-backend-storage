#!/usr/bin/env python3
"""interpreter used"""

from pymongo import MongoClient


if __name__ == "__main__":
    """ a Python script that provides some stats about Nginx logs stored in MongoDB:"""
        client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_data = client.logs.nginx

    nginx_logs = nginx_data.count_documents({})
    print(f"{nginx_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx_data.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status = nginx_data.count_documents({"method": "GET", "path": "/status"})
    print(f"{status} status check")
