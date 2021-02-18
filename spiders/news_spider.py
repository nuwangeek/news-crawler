import scrapy
from ..items import NewsscraperItem

class NewsSpider(scrapy.Spider):
    name = 'news'
    start_urls = [
        'https://divaina.com/sunday/index.php/hot-news'
    ]

    def parse(self, response):
        items = NewsscraperItem()
        #response contains sourc code of the web page
        all_hot_news = response.css('.col-lg-12 .bt-inner')

        for hotnews in all_hot_news:
            title = hotnews.css('a.bt-title::text').extract()
            content = hotnews.css('.bt-introtext::text').extract()
            items['title'] = title
            items['content'] = content

            yield items




