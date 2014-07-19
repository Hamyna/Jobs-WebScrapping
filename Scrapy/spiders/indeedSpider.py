__author__ = 'hamyna'
__author__ = 'hamyna'
# this class is a spider class for www.indeed.com
# this class will define the structure of data we want to scrap from indeed based on the site structure

import scrapy
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from Scrapy.items import IndeedItem

class indeedSpider(scrapy.Spider):
    name = "indeed"
    #indeed domain, domain we are intending to scrap
    allowed_domains = ["www.indeed.ca"]
    # list of urls from that domain to crawl
    start_urls = ["http://www.indeed.ca/jobs?q=it&l=BC",
                  "http://www.indeed.ca/jobs?q=developer&l=BC",
                  "http://www.indeed.ca/jobs?q=programming&l=BC",
                  "http://www.indeed.ca/jobs?q=software&l=BC",
                  "http://www.indeed.ca/jobs?q=data+analytics&l=BC",
                  "http://www.indeed.ca/jobs?q=IT+consultant&l=BC",
                  "http://www.indeed.ca/jobs?q=+IT+analyst&l=BC"]
    rules = (Rule(SgmlLinkExtractor(allow=("http://www.indeed.ca/cmp/", "http://www.indeed.ca/rc/clk?jk=",),restrict_xpaths=('//a[@class="button next"]',))
    ,callback="parse", follow= True),)

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
            hxs = HtmlXPathSelector(response)
        titles = hxs.select('//span[@class="pl"]')
        items = []
        for titles in titles:
            item = IndeedItem()
            item ["title"] = titles.select("a/text()").extract()
            items.append(item)
        return(items)

