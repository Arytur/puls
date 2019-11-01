import scrapy


class ShopingItem(scrapy.Item):
    url = scrapy.Field()
    price = scrapy.Field()