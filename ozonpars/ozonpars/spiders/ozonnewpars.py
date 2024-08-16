import scrapy


class OzonnewparsSpider(scrapy.Spider):
    name = "ozonnewpars"
    allowed_domains = ["https://ozon.ru"]
    start_urls = ["https://www.ozon.ru/category/noutbuki-15692/"]

    def parse(self, response):
        nouts = response.css('div.j7m_23')

        for nout in nouts:
            yield {
                'name' : nout.css('div.kj2_23 span::text').get(),
                'price' : nout.css('div.c3013-a0 span::text').get(),
                'url' : nout.css('a').attrib['href']
            }

