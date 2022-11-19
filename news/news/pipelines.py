# Define your item pipelines here

import pymongo
import os
import sys
from scrapy.utils.project import get_project_settings


class MongoDBPipeline(object):
    def __init__(self):

        settings = get_project_settings()
        host=settings.get('MONGODB_HOST')
        db = settings.get('MONGODB_DB')
        coll = settings.get('MONGODB_COLLECTION')

        connection =pymongo.MongoClient(host)
        db = connection[db]
        self.collection = db[coll]

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item
