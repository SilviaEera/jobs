# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class JobSpider(CrawlSpider):
    name = 'job'
    allowed_domains = ['www.irishjobs.ie']
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"

    def start_requests(self):
        yield scrapy.Request(url = "http://www.irishjobs.ie/ShowResults.aspx?Keywords=python+&autosuggestEndpoint=%2Fautosuggest&Location=0&Category=&Recruiter=Company&Recruiter=Agency&btnSubmit=Search/", headers= {
            'User-Agent': self.user_agent
        })
    rules = (
        Rule(LinkExtractor(restrict_xpaths= "//div[@class='job-result-title']/h2/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths= "//a[@class='alt']"))
    )

    def set_user_agent(self, request):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        yield {
            'Job Title': response.xpath("//div[@class='job-description']/h1/text()").get(),
            'Company Name': response.xpath("//div[@class='job-description']/h2/text()").get(),
            'Location': response.xpath("//li[@class='location']/text()").get(),
            'Salary': response.xpath("//li[@class='salary']/text()").get(),
            'Job Type': response.xpath("//li[@class='employment-type']/text()").get(),
            'Job Posted': response.xpath("//li[@class='updated-time']/text()").get(),
            'Company Address': response.xpath("//li[@class='address']/text()").get(),
            'Company Contact': response.xpath("//li[@class='telnum']/text()").get(),
            'Company Website': response.xpath("//li[@class='url']/a/@href").get(),
            'Job Link': response.request.url
        }
