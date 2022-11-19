# Scrapy settings for news project
MONGODB_HOST = 'mongodb+srv://ambalatharasu:nakheel@ambalatharasu.eftsitr.mongodb.net/?retryWrites=true&w=majority'
MONGODB_DB ='Nakheel'
MONGODB_COLLECTION= 'CNN_NEWS'
NEWS_URL='https://edition.cnn.com/world/live-news/coronavirus-pandemic-06-25-20-intl/index.html'
BOT_NAME = 'news'
SPIDER_MODULES = ['news.spiders']
NEWSPIDER_MODULE = 'news.spiders'
ROBOTSTXT_OBEY = True
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
ITEM_PIPELINES = {
    'news.pipelines.MongoDBPipeline' : 100,
}
