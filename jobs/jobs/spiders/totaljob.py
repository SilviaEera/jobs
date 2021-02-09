# -*- coding: utf-8 -*-
import scrapy


class TotaljobSpider(scrapy.Spider):
    name = 'totaljob'
    allowed_domains = ['www.totaljobs.com/jobs/python?s=header']
    #start_urls = ['https://www.totaljobs.com/jobs/python?s=header/']

    def start_requests(self):
        yield scrapy.Request(url= 'https://www.totaljobs.com/jobs/python?s=header/', callback= self.parse, headers={
            'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
        })

    def parse(self, response):
        for product in response.xpath("//div[@class='job   ']"):
            return

