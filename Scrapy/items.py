# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    pass

class IndeedItem(scrapy.Item):
    title = scrapy.Field()
    about = scrapy.Field()
    description = scrapy.Field()
    location = scrapy.Field()
    company = scrapy.Field()
    education = scrapy.Field()
    skills = scrapy.Field()
    salary = scrapy.Field()
    contact = scrapy.Field()

class MonsterItem(scrapy.Item):
    title = scrapy.Field()
    about = scrapy.Field()
    description = scrapy.Field()
    skills = scrapy.Field()
    responsibilities = scrapy.Field()
    location = scrapy.Field()
    company = scrapy.Field()
    education = scrapy.Field()
    salary = scrapy.Field()
    contact = scrapy.Field()