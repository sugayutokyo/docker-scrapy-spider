import scrapy


class GethtmlSpider(scrapy.Spider):
    name = "getHtml"
    allowed_domains = ["zenn.dev"]
    start_urls = ["https://zenn.dev"]

    def parse(self, response):
        pass
