#!/usr/bin/env python3
""" 12-log_stats.py """
import pymongo


if __name__ == '__main__':
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    collection = client.logs.nginx
    print(f'{collection.count_documents({})} logs')
    print('Methods:')
    for method in methods:
        print(f'\tmethod {method}: {collection.count_documents({"method": method})}')
    print(f'{collection.count_documents({"method": "GET", "path": "/status"})} status check')
