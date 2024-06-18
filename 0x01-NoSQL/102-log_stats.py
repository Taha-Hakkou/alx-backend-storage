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
    # Sorted top 10 of the most present IPs in the collection nginx
    requests = collection.aggregate([
        { '$group':
            { '_id':
                { 'ip': '$ip' },
                'count': { '$sum': 1 }
            }
        },
        { '$sort':
            {'count': pymongo.DESCENDING}
        },
        { '$limit': 10 }
    ])
    print('IPs:')
    for request in requests:
        print(f"\t{request.get('_id').get('ip')}: {request.get('count')}")
