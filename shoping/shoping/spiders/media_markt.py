import scrapy


class MediaMarktSpider(scrapy.Spider):
    name = 'media_markt'
    start_urls = []

    pattern = ''

    def parse(self, response):
        findings = response.xpath(self.pattern).getall()
        print(findings)
