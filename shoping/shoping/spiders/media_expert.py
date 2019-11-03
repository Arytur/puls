import logging
import scrapy

from ..items import ShopingItem

from app.models import ProductInShop, Shop

logger = logging.getLogger(__name__)

class MediaExpertSpider(scrapy.Spider):
    name = 'media_expert'
    shop = Shop.objects.get(name="mediaexpert")
    products = ProductInShop.objects.filter(shop=shop).values_list("url", flat=True) 
    
    logger.info('Spider started for %d pages', len(products))
    start_urls = list(products) 

    def parse(self, response):
        pattern = '//div[has-class("buy_info_price")]//p[has-class("price")]//text()'
        findings = response.xpath(pattern).getall()
        logger.debug('Found: %s, url: %s', findings, response.url)
        assert len(findings) == 4, "Price occurence different than 4"
        assert findings[:2] == findings[2:], "Prices are different"
        item = ShopingItem()
        item['url'] = response.url
        # take first pair from results (whole price)
        item['price'] = '.'.join(findings[:2])
        yield item
