import scrapy

class BookList_Spider(scrapy.Spider):
    name = 'booklist'

    allowed_domains = [

    ]
    start_urls = [
        ''
    ]

    def parse(self, response):
        pass