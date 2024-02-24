import scrapy

class EbookSpider(scrapy.Spider):
    name = "ebook1"
    start_urls = ['https://books.toscrape.com/']

    def parse(self,response):
        print("*********[Parse]************")

        print("CSS :",response.css("h3 a")[0])

        print("Xpath :",response.xpath("//h3/a/text()")[0])