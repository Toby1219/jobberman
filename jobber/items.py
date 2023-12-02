# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    # define the fields for your item here like:
    job_tittle = scrapy.Field()
    commpany_Name = scrapy.Field()
    sector = scrapy.Field()
    pay = scrapy.Field()
    minimum_qualification = scrapy.Field()
    experience_level = scrapy.Field()
    experience_length = scrapy.Field()
    responsibilities = scrapy.Field()
    requirements = scrapy.Field()
