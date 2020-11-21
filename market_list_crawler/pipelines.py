# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from .controller.price_controller import PriceController




class MarketListCrawlerPipeline:

    def __init__(self):
        self.pc = PriceController()
    def process_item(self, item, spider):
        self.pc.insert(item)
        return item
