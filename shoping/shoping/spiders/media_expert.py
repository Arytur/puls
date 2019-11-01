import scrapy
from ..items import ShopingItem


class MediaExpertSpider(scrapy.Spider):
    name = 'media_expert'
    start_urls = [
        'https://www.mediaexpert.pl/blendery/blender-bosch-msm-88190,id-241817'
    ]

    def parse(self, response):
        pattern = '//div[has-class("buy_info_price")]//p[has-class("price")]//text()'
        findings = response.xpath(pattern).getall()
        print(findings)
        assert len(findings) == 4, "Price occurence different than 4"
        assert findings[:2] == findings[2:], "Prices are different"
        item = ShopingItem()
        item['url'] = self.start_urls[0]
        item['price'] = '.'.join(findings[:2])
        yield item
