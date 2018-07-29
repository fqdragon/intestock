# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy_splash import SplashRequest

class IntstockSpider(scrapy.Spider):
    name = 'intestock'
    allowed_domains = ['quote.eastmoney.com/']
    start_urls = ['http://quote.eastmoney.com/sz000839.html']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait':0.5})

    def parse(self, response):
        sel = Selector(response)
        price = sel.xpath("//div[@id='arrowud']/strong[@id='price9']").extract_first()
        print(price)
        pass
