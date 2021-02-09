# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TotaljobsSpider(CrawlSpider):
    name = 'totaljobs'
    allowed_domains = ['www.totaljobs.com']
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"

    def start_requests(self):
        yield scrapy.Request(url = "https://www.totaljobs.com/jobs/python?s=header/", headers= {
            'User-Agent': self.user_agent
        })

    rules = (
        Rule(LinkExtractor(restrict_xpaths= "//div[@class='job-title']/a"), callback='parse_item', follow=True),
    )
    def set_user_agent(self, request):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        yield {
            'Job Title': response.xpath("//h1[@class='brand-font']/text()").get(),
            'Company Name': response.xpath("//a[@id='companyJobsLink']/text()").get(),
            'Location': response.xpath("//a[@class='engagement-metric']/text()").get(),
            'Salary': response.xpath("//li[@class='salary icon']/div/text()").get(),
            'Job Type': response.xpath("//li[@class='job-type icon']/div/text()").get(),
            'Job Posted': response.xpath("//li[@class='date-posted icon']/div/span/text()").get(),
            'Job Link': response.request.url
        }