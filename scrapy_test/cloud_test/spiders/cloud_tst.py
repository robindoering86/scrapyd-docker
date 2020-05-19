# -*- coding: utf-8 -*-
import scrapy
import json
from cloud_test.items import CloudTestItem


class CloudTstSpider(scrapy.Spider):
    name = 'cloud_tst'
    allowed_domains = ['httpbin.org']
    start_urls = [f'https://httpbin.org/anything/{i}' for i in range(1, 10)]

    def parse(self, response):
        js = json.loads(response.text)
        item = CloudTestItem()
        item['ip'] = js.get('origin')
        item['headers']  = js.get('headers')
        yield item
