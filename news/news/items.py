# Define here the models for your scraped items
#
# See documentation in:

from scrapy.item import Item, Field
class NewsItem(Item):
    news = Field()
    article = Field()
    author = Field()
    articledate = Field()