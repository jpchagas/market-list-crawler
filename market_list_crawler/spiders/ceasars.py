import scrapy
from ..utils import date_helper as dh


class CeasarsSpider(scrapy.Spider):
    name = 'ceasars'
    allowed_domains = [r'http://ceasa.rs.gov.br/']
    #start_urls = [self.url]
    start_urls = [r'http://ceasa.rs.gov.br/tabcotacao/15-09-2020/']

    def parse(self, response):
        for row in response.xpath('//table/tbody/tr'):
            yield {
                'produto': row.xpath('td[1]//text()').extract_first(),
                'unidade': row.xpath('td[2]//text()').extract_first(),
                'maximo': row.xpath('td[3]//text()').extract_first(),
                'frequente': row.xpath('td[4]//text()').extract_first(),
                'minimo': row.xpath('td[5]//text()').extract_first(),
            }