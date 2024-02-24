import scrapy

class EbookSpider(scrapy.Spider):
    name = "ebook"
    start_urls = ['https://books.toscrape.com/']

    def parse(self,response):
        print("*********[Parse]************")

        #print(response.css("h3 a::text").get())
        books = response.css("article")
        
        for book in books:
            title = book.css("a::text").get()
            price = book.css("p.price_color::text").get()
            #print(title,price)

            yield{
                "title":title,
                "price":price
            }
