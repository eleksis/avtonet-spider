# -*- coding: utf-8 -*-
from scrapy import Spider


class NewCarSpider(Spider):

    def parse(self, response):
        ads = response.css('.ResultsAdPhotoTop a::attr(href)').extract()
        for car in ads:
            yield {'id': car.split('=')[-1], 'link': response.urljoin(car)}

        for a in response.css('#navi123 a'):
            yield response.follow(a, callback=self.parse)
