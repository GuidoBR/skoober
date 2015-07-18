import scrapy


class SkoobSpider(scrapy.Spider):
    name = "skoob"
    start_urls = ['http://skoob.com.br/']

    def parse(self, response):
        print(response.url)
