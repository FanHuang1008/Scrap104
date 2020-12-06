# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Scrap104Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    company = scrapy.Field()
    region = scrapy.Field()
    salary = scrapy.Field()
    competitor = scrapy.Field()
    link = scrapy.Field()
    pass
