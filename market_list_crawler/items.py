# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MarketListCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    produto = scrapy.Field()
    unidade = scrapy.Field()
    maximo = scrapy.Field()
    frequente = scrapy.Field()
    minimo = scrapy.Field()
    data = scrapy.Field()
