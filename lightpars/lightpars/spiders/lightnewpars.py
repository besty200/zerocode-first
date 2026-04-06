import scrapy
import csv


class LightnewparsSpider(scrapy.Spider):
    name = "lightnewpars"
    allowed_domains = ["https://minimir.ru"]
    start_urls = ["https://minimir.ru/catalog/interernoe-osveshchenie/lustri"]

    def parse(self, response):
        parsed_data=[]
        lights = response.css('div.info')
        for light in lights:
            yield {
                'name' : light.css('div.h6 a::text').get(),
                'price' : (light.css('div.col-auto span::text').get().replace('\xa0'," ")).replace('\u2009', ''),
                'url' : light.css('a').attrib['href']
            }
            parsed_data.append([light.css('div.h6 a::text').get(), (light.css('div.col-auto span::text').get().replace('\xa0'," ")).replace('\u2009', ''), light.css('a').attrib['href']])
        with open("hh.csv", 'w', newline='', encoding='utf-8') as file:
            # Используем модуль csv и настраиваем запись данных в виде таблицы
            # Создаём объект
            writer = csv.writer(file)
            # Создаём первый ряд
            writer.writerow(['Название', 'цена', 'ссылка'])
            # Прописываем использование списка как источника для рядов таблицы
            writer.writerows(parsed_data)

