import scrapy
import csv
from castorama.items import ProductItem
import time

class ProductspiderSpider(scrapy.Spider):
    name = "productspider"
    allowed_domains = ["www.castorama.fr"]
    
    def start_requests(self):
        with open('categories.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[-1] != "url":
                    yield scrapy.Request(
                        url = row[-1],
                        callback=self.parse,
                        meta={"url" : row[-1]}
                    )
        
    def parse(self, response):
        products = response.css('ul#product-lister > li')
        
        for prod in products:
            prod_text = prod.css('p::text').get()
            
            url = response.meta["url"]
            prod_url = url + prod.css('a').attrib['href']
            prod_prix = prod.css('div._5d34bd7a ::text').get()
            cat = url[25:].split('/')
            unique = prod.css('a').attrib['href'].split('/')
            
            time.sleep(2)
            productitem = ProductItem()

            productitem["url"] = prod_url,
            productitem["category"] = cat[0],
            productitem["subcategory"] = cat[1],
            productitem["subsubcategory"] = cat[2],
            productitem["subsubsubcategory"] = cat[3],
            productitem["unique_id"] = unique[-1],
            productitem["title"] = prod_text,
            productitem["price"] = prod_prix,


            yield productitem

        next_page = response.css('#Next\ page\ button > a:nth-child(1)::attr(href)').get()

        if next_page is not None:
            next_page_url = "https://www.castorama.fr" + next_page
            yield response.follow(next_page_url, callback=self.parse, meta={"url" : url})
        
        else:
            print("no more page")

