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

    print(f"{logs} logs")
    print("Methods:")
    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")
    print(f"{status_check} status check")


    doc = nginx_collection.find({"ip": {"$exists": True}})
    doclist = [x['ip'] for x in doc]
    my_dict = {x: doclist.count(x) for x in set(doclist)}
    sorted_dict= dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True)[:10])
    print("IPs:")
    for key, value in sorted_dict.items():
        print(f"\t{key}: {value}")
        

