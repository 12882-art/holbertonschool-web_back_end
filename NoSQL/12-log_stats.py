#!/usr/bin/env python3
"""Log stats"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    
    # Count total logs
    total = logs.count_documents({})
    print(f"{total} logs")
    
    # Methods count
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = logs.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    
    # Status check count
    status_check = logs.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")
