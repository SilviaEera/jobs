# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class GradirelandSpider(CrawlSpider):
    name = 'gradireland'
    allowed_domains = ['gradireland.com']
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    #start_urls = ['https://gradireland.com/search/all/focus/ad_vacancy/focus/ad_organisation#query=python&sort_by=search_api_relevance/']

    def start_requests(self):
        yield scrapy.Request(url= "https://gradireland.com/search/all/focus/ad_vacancy/focus/ad_organisation#query=python&sort_by=search_api_relevance/", headers= {
            'User-Agent': self.user_agent
        })

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='pane-content']/h3/a"), callback='parse_item', follow=True),
    )

    def set_user_agent(self, request):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        yield {
            'Job Title': response.xpath("//div[@class='pane-content']/h2/text()").get(),
            'Company Name': response.xpath("//div[@class='panel-pane pane-block pane-block-137 pane-block']/div/h2/text()").get(),
            'Deadline': response.xpath(" //span[@class='date-display-single']/text()").get(),
            'Job Link': response.request.url
        }
