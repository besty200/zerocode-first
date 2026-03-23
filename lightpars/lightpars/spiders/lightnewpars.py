import scrapy


class LightnewparsSpider(scrapy.Spider):
    name = "lightnewpars"
    allowed_domains = ["https://minimir.ru"]
    start_urls = ["https://minimir.ru/catalog/interernoe-osveshchenie/lustri"]

    def parse(self, response):
        lights = response.css('div.info')
        for light in lights:
            yield {
                'name' : light.css('div.h6 a::text').get(),
                'price' : light.css('div.col-auto span::text').get(),
                'url' : light.css('a').attrib['href']
            }

