# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class SteamgamesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()

    link = scrapy.Field()

    time = scrapy.Field()

    evaluate = scrapy.Field()

    discount = scrapy.Field()

    price = scrapy.Field()
    #pass
