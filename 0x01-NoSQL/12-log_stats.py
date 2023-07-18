#!/usr/bin/env python3
"""pymongo script"""
from pymongo import MongoClient


if __name__ == "__main__":
    """function module"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    logs = nginx_collection.count_documents({})
    get = nginx_collection.count_documents({"method": "GET"})
    post = nginx_collection.count_documents({"method": "POST"})
    put = nginx_collection.count_documents({"method": "PUT"})
    patch = nginx_collection.count_documents({"method": "PATCH"})
    delete = nginx_collection.count_documents({"method": "DELETE"})
    status_check = nginx_collection.count_documents({"path": "/status"})

    print(f"{logs} logs", end="")
    print(f"""
    Methods:
        method GET: {get}
        method POST: {post}
        method PUT: {put}
        method PATCH: {patch}
        method DELETE: {patch}
    {status_check} status check
    """, end="")
