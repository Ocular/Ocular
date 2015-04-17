# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OcularItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    guid = scrapy.Field()
    id = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    time = scrapy.Field()
    version = scrapy.Field()
    author = scrapy.Field()
    tag = scrapy.Field()
    extra = scrapy.Field()
