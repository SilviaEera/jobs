# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class JobrapidoSpider(CrawlSpider):
    name = 'jobrapido'
    allowed_domains = ['ie.jobrapido.com']
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"

    def start_requests(self):
        yield scrapy.Request(url = "https://ie.jobrapido.com/?w=python", headers= {
            'User-Agent': self.user_agent
        })

    rules = (
        Rule(LinkExtractor(restrict_xpaths= "//div[@class='result-item__save-job-box']/a"), callback='parse_item', follow=True),
    )

    def set_user_agent(self, request):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        yield {
            'Job Title': response.xpath("//h1[@class='job__title']/span[1]").get(),
            'Company Name': response.xpath("//p[@class='job__header-posted sm-no']/span/a/text()").get(),
            'Location': response.xpath("(//dd[@class='job__details-value'])[1]/text()").get(),
            'Salary': response.xpath("(//dd[@class='job__details-value'])[2]/text()").get(),
            'Job Type': response.xpath("(//dd[@class='job__details-value'])[3]/text()").get(),
            'Job Posted': response.xpath("//p[@class='job__header-posted sm-no']/span[2]/text()").get(),
            'Contract Length': response.xpath("(//dd[@class='job__details-value'])[4]/text()").get(),
            'Job ID': response.xpath("(//dd[@class='job__details-value'])[7]/text()").get(),
            'Company Website': response.xpath("//p[@class='job__header-posted sm-no']/span/a/@href").get(),
            'Job Link': response.request.url
        }