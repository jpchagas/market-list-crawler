import scrapy
from ..utils import date_helper as dh
from ..utils import url_helper as uh
from ..items import MarketListCrawlerItem
from scrapy.loader import ItemLoader


class CeasarsSpider(scrapy.Spider):
    name = 'ceasars'
    allowed_domains = [r'http://ceasa.rs.gov.br/']
    #start_urls = [r'http://ceasa.rs.gov.br/tabcotacao/07-04-2020/']

    def start_requests(self):
        urls = uh.generate_url()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        dia = response.xpath("//header/h1/text()").get()
        if dia[0] == 'C':
            dia = dia[8:]

        for row in response.xpath('//table/tbody/tr'):
            l = ItemLoader(item=MarketListCrawlerItem(), selector=row)
            l.add_xpath('produto', "td[1]//text()")
            l.add_xpath('unidade', "td[2]//text()")
            l.add_xpath('maximo', "td[3]//text()")
            l.add_xpath('frequente', "td[4]//text()")
            l.add_xpath('minimo', "td[5]//text()")
            l.add_value('data', dia.replace('/', '-'))
            #l.add_value('data', dh.current_date())
            l.add_value('origem', "CEASARS")
            yield l.load_item()
            '''
            yield {
                'produto': row.xpath('td[1]//text()').extract_first(),
                'unidade': row.xpath('td[2]//text()').extract_first(),
                'maximo': row.xpath('td[3]//text()').extract_first(),
                'frequente': row.xpath('td[4]//text()').extract_first(),
                'minimo': row.xpath('td[5]//text()').extract_first(),
            }
            '''