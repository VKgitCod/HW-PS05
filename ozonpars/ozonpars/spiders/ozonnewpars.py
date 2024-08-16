import scrapy


class OzonnewparsSpider(scrapy.Spider):
    name = "ozonnewpars"
    allowed_domains = ["https://ozon.ru"]
    start_urls = ["https://www.ozon.ru/category/noutbuki-15692/"]

    def parse(self, response):
        pass
