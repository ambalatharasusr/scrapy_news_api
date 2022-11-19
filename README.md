Details

Write an application to crawl an online news website, e.g. www.theguardian.com/au or www.bbc.com using your choice of crawler framework such as [Scrapy] (http://scrapy.org/) and build the application in Python.

The application should cleanse the articles to obtain only information relevant to the news story, e.g. article text, author, headline, article url, etc. Use a framework such as Readability to cleanse the page of superfluous content such as advertising and html

Store the data in a hosted mongo database, e.g. compose.io/mongo, for subsequent search and retrieval. Ensure the URL of the article is included to enable comparison to the original.

Write an API that provides access to the content in the mongo database. The user should be able to search for articles by keyword.
