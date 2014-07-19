__author__ = 'hamyna'
__author__ = 'hamyna'
__author__ = 'hamyna'
# this class is a spider class for www.indeed.com
# this class will define the structure of data we want to scrap from indeed based on the site structure

import scrapy
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from Scrapy.items import MonsterItem
#scrapy crawl craig -o items.csv -t csv
class monsterSpider(CrawlSpider):
    name = "monster"
    #indeed domain, domain we are intending to scrap
    allowed_domains = ["www.monster.ca"]
    # list of urls from that domain to crawl
    start_urls = ["http://jobview.monster.ca/Junior-Intermediate-Data-Analyst-Job-Burnaby-BC-CA-136319726.aspx",
                  "http://jobview.monster.ca/Data-Analyst-Job-Burnaby-BC-CA-136683877.aspx",
                  "http://jobview.monster.ca/Treasury-Financial-Analyst-Job-Vancouver-BC-CA-136659502.aspx",
                  "http://jobview.monster.ca/Treasury-Financial-Analyst-Job-Vancouver-BC-CA-136659502.aspx",
                  "http://jobview.monster.ca/GIS-Programmer-Analyst-Job-Vancouver-BC-CA-136056624.aspx",
                  "http://jobview.monster.ca/REVENUE-ANALYST-Job-Victoria-BC-CA-136057973.aspx",
                  "http://jobview.monster.ca/QA-Analyst-Job-Burnaby-BC-CA-136598576.aspx",
                  "http://jobview.monster.ca/Central-Procurement-Inventory-Analyst-Job-Richmond-BC-CA-136554418.aspx",
                  "http://jobview.monster.ca/Systems-Analyst-Job-Vancouver-BC-CA-136549246.aspx",
                  "http://jobview.monster.ca/Business-Systems-Analyst-Job-Vancouver-BC-CA-136549367.aspx",
                  "http://jobview.monster.ca/Technical-Support-Analyst-Job-Richmond-BC-CA-135808920.aspx",
                  "http://jobview.monster.ca/Senior-Financial-Analyst-Job-Vancouver-BC-CA-136523899.aspx",
                  "http://jobview.monster.ca/BI-Developer-Analyst-Job-Vancouver-BC-CA-135934336.aspx",
                  "http://jobview.monster.ca/Financial-Analyst-Job-Burnaby-BC-CA-135320720.aspx",
                  "http://jobview.monster.ca/Technical-Analyst-Voice-Systems-Job-Vancouver-BC-CA-136490017.aspx",
                  "http://jobview.monster.ca/Quality-Assurance-Analyst-Job-Vancouver-BC-CA-136433771.aspx",
                  "http://jobview.monster.ca/Senior-Programmer-Analyst-Supply-Chain-Job-Vancouver-BC-CA-135828770.aspx",
                  "http://jobview.monster.ca/Senior-Programmer-Analyst-Business-Intelligence-Job-VANCOUVER-BC-CA-136359740.aspx",
                  "http://jobview.monster.ca/Intermediate-Systems-Analyst-Job-Vancouver-BC-CA-136358215.aspx",
                  "http://jobview.monster.ca/HRIS-Business-Developer-Intelligence-Analyst-Job-Vancouver-BC-CA-136265100.aspx",
                  "http://jobview.monster.ca/IP-Engineering-Analyst-Job-Vancouver-BC-CA-136055348.aspx",
                  "http://jobview.monster.ca/Management-Consulting-Business-Analyst-Job-Vancouver-BC-CA-126324946.aspx",
                  "http://jobview.monster.ca/Intermediate-Support-Analyst-Job-Richmond-BC-CA-135630233.aspx",
                  "http://jobview.monster.ca/Business-Analyst-Senior-Job-Capitol-Region-Island-BC-CA-135116587.aspx",
                  "http://jobview.monster.ca/PeopleSoft-Finance-Functional-Analyst-all-regions-Canada-Job-Vancouver-BC-CA-136638546.aspx",
                  "http://jobview.monster.ca/PeopleSoft-HRMS-Functional-Analyst-all-regions-Canada-Job-Vancouver-BC-CA-136638772.aspx",
                  "http://jobview.monster.ca/PeopleSoft-HRMS-Functional-Analyst-%e2%80%93-NA-Payroll-Time-Labor-all-regions-Canada-Job-Vancouver-BC-CA-136638966.aspx",
                  "http://jobview.monster.ca/PeopleSoft-Financial-Technical-Developer-Analyst-all-regions-Canada-Job-Vancouver-BC-CA-136638598.aspx",
                  "http://jobview.monster.ca/GIS-Programmer-Analyst-Job-Vancouver-BC-CA-136056624.aspx",
                  "http://jobview.monster.ca/Systems-Analyst-Job-Vancouver-BC-CA-136549246.aspx",
                  "http://jobview.monster.ca/Business-Systems-Analyst-Job-Vancouver-BC-CA-136549367.aspx",
                  "http://jobview.monster.ca/Information-Systems-Security-Analyst-Job-Vancouver-BC-CA-136533537.aspx",
                  "http://jobview.monster.ca/Business-Analyst-Change-Management-Experience-Job-Vancouver-BC-CA-136533728.aspx",
                  "http://jobview.monster.ca/Business-Analyst-Navision-Job-Vancouver-BC-CA-136531425.aspx",
                  "http://jobview.monster.ca/Senior-Business-Systems-Analyst-Retail-Job-Vancouver-BC-CA-135320552.aspx",
                  "http://jobview.monster.ca/Financial-Analyst-Job-Burnaby-BC-CA-135320720.aspx",
                  "http://jobview.monster.ca/Technical-Analyst-Voice-Systems-Job-Vancouver-BC-CA-136490017.aspx",
                  "http://jobview.monster.ca/Junior-Business-Analyst-Job-Vancouver-BC-CA-136477331.aspx",
                  "http://jobview.monster.ca/Senior-Business-Analyst-Claims-Processing-Job-Vancouver-BC-CA-135890708.aspx",
                  "http://jobview.monster.ca/Quality-Assurance-Analyst-Job-Vancouver-BC-CA-136433771.aspx",
                  "http://jobview.monster.ca/Senior-Programmer-Analyst-Supply-Chain-Job-Vancouver-BC-CA-135828770.aspx",
                  "http://jobview.monster.ca/Senior-Programmer-Analyst-Business-Intelligence-Job-VANCOUVER-BC-CA-136359740.aspx",
                  "http://jobview.monster.ca/Intermediate-Systems-Analyst-Job-Vancouver-BC-CA-136358215.aspx",
                  "http://jobview.monster.ca/SOX-Analyst-Job-Burnaby-BC-CA-136329900.aspx",
                  "http://jobview.monster.ca/Service-Desk-Analyst-Job-Vancouver-BC-CA-136320493.aspx",
                  "http://jobview.monster.ca/HRIS-Business-Developer-Intelligence-Analyst-Job-Vancouver-BC-CA-136265100.aspx",
                  "http://jobview.monster.ca/Junior-HelpDesk-Analyst-Job-Vancouver-BC-CA-136058196.aspx",
                  "http://jobview.monster.ca/Management-Consulting-Business-Analyst-Job-Vancouver-BC-CA-126324946.aspx",
                  "http://jobview.monster.ca/Testing-Analyst-Job-Burnaby-BC-CA-136004566.aspx"]

    rules = (Rule(SgmlLinkExtractor(allow_domains=("jobview.monster.ca"), deny_domains=("jobsearch.monster.ca"), restrict_xpaths=('//a[@class="page_navigation"]',)),callback="parse", follow= True),)

    def parse(self, response):
        """ Extract job tile, roles, responsibility, location,education and skills using XPath selectors """
        #self.log('A response from %s just arrived!' % response.url)
        #hxs = HtmlXPathSelector(response)
        item = MonsterItem()
        #extract title

        for title in response.xpath('//head/title').extract():
            if not title:
                for title in response.xpath('//div//h1/text()').extract():
                    yield MonsterItem(title=title)
            else:
                yield MonsterItem(title=title)
        for about in response.xpath('//div//span//p//span//text()').extract():
            yield MonsterItem(about=about)
        for about in response.xpath('//div//span//p//span//text()').extract():
            yield MonsterItem(about=about)
        for skills in response.xpath('//div//span//ul//li//text()').extract():
           yield MonsterItem(skills=skills)
