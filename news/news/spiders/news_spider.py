from scrapy import Spider
from scrapy.selector import Selector
from ..items import NewsItem
from scrapy.utils.project import get_project_settings
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from urllib.parse import urlparse
import time

class StackSpider(Spider):
    name = "news"
    rules = (
        Rule(
            LinkExtractor(allow=(), unique=True),
            callback='parse',
            follow=True
        ),
    )
    settings = get_project_settings()
    url = settings.get('NEWS_URL')

    start_urls = [
        url
    ]

    def parse(self, response):
        all_div_quotes=Selector(response).xpath('//article[contains(@class, "sc-bwzfXH sc-eXEjpC iGQwpp")]')
        item = NewsItem()
        i=0
        for quotes in all_div_quotes:
            i += 1
            try:
                news = quotes.xpath("//h2[@class='sc-dfVpRl kvaBeP']/text()").extract()[i].strip()
                item['news'] = news
                article = quotes.xpath("//p[@class='sc-gZMcBi render-stellar-contentstyles__Paragraph-sc-9v7nwy-2 dCwndB']/text()").extract()[i].strip()
                item['article'] = article
                articledate = quotes.xpath("//span[@class='sc-iujRgT llASnG']/text()").extract()[i].strip()
                item['articledate'] = articledate
                author = quotes.xpath("//p[@class='sc-gzOgki ixpUvU']/text()").extract()[i].strip()
                item['author'] = author
                yield item
            except:
                print("An exception occurred")
        return item



