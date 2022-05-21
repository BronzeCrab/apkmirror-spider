# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ApkmirrorItem(scrapy.Item):
    download_link = scrapy.Field()
    apk_link = scrapy.Field()
    version = scrapy.Field()
    uploaded = scrapy.Field()
    file_size = scrapy.Field()
    downloads = scrapy.Field()
