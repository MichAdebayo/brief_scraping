import scrapy
import csv

class ProductspiderSpider(scrapy.Spider):
    name = "productspider"
    allowed_domains = ["www.castorama.fr"]
    
    def start_requests(self):
        with open('castospider.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                yield scrapy.Request(
                    url = row[0],
                    callback=self.parse,
                    meta={"url" : row[0]}
                )
    
    def parse(self, response):
        products = response.css('ul#product-lister > li')
        
        for prod in products:
            prod_text = prod.css('p::text').get()
            
            url = response.meta["url"]
            prod_url = url + prod.css('a').attrib['href']
            prod_prix = prod.css('div._5d34bd7a ::text').get()
            cat = url[25:].split('/')
            yield {
                "category" : cat[0],
                "subcategory": cat[1],
                "subsubcategory": cat[2],
                "subsubsubcategory": cat[3],
                "title" : prod_text,
                "prix" : prod_prix,
                "prod_url" : prod_url,
            }

        next_page = response.css('#Next\ page\ button > a:nth-child(1)::attr(href)').get()

        if next_page is not None:
            next_page_url = "https://www.castorama.fr" + next_page
            yield response.follow(next_page_url, callback=self.parse, meta={"url" : url})
        
        else:
            print("no more page")

