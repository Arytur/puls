import logging
import re
import scrapy

from ..items import ShopingItem

from app.models import ProductInShop, Shop

logger = logging.getLogger(__name__)

class WrowroSpider(scrapy.Spider):
    name = 'wrowro'
    shop = Shop.objects.get(name="wrowro")
    products = ProductInShop.objects.filter(shop=shop).values_list("url", flat=True) 
    
    logger.info('%s spider started for %d pages', shop, len(products))
    start_urls = list(products) 

    def parse(self, response):
        pattern = '//div[has-class("price")]//em[has-class("main-price")]//text()'
        findings = response.xpath(pattern).get()
        logger.debug('Found: %s, url: %s', findings, response.url)
        get_price = re.findall(r'\d+', findings)
        item = ShopingItem()
        item['url'] = response.url
        item['price'] = '.'.join(get_price)
        yield item
