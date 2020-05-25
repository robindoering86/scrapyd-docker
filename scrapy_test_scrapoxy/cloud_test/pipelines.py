# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import pymongo


class MongoPipeline(object):

    collection_name = 'test'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        ## pull in information from settings.py
        MONGO_USER = crawler.settings.get('MONGO_USER'),
        MONGO_DB = crawler.settings.get('MONGO_DB'),        
        return cls(
            mongo_uri = f'{crawler.settings.get("MONGO_URI")}',
            mongo_db = crawler.settings.get('MONGO_DATABASE'),
        )

    def open_spider(self, spider):
        ## initializing spider
        ## opening db connection
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        ## clean up when spider is closed
        self.client.close()

    def process_item(self, item, spider): 
        ## how to handle each post
        item = dict(item)
        item = {
            'ip': item.get('ip'),
            'headers': item.get('headers'),
        }
        doc_exists = self.db[self.collection_name].find_one(
            {'ip': item.get('ip')}
            )
        self.db[self.collection_name].insert_one(item)
        logging.debug(f'Added new document to MongoDB')

        return item
