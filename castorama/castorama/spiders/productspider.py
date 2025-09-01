import scrapy
import csv
from castorama.items import ProductItem

class ProductspiderSpider(scrapy.Spider):
    """
    Spider for scraping product information from the Castorama website.
    Initiates requests from category URLs and parses product listings and pagination.

    Attributes:
        name: The name of the spider.
        allowed_domains: List of domains allowed for scraping.
    """
    name = "productspider"
    allowed_domains = ["www.castorama.fr"]
    
    def start_requests(self):
        """
        Reads category URLs from a CSV file and initiates requests for each category.
        Skips the header row and yields requests with the category URL in the meta data.

        Yields:
            scrapy.Request: A request for each category URL found in the CSV file.
        """
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
        """
        Parses the product listing page and yields ProductItem objects for each product found.
        Also follows pagination links to scrape additional product pages.

        Args:
            response: The response object for the current page.

        Yields:
            ProductItem: An item containing product details for each product found.
            scrapy.Request: A request to the next page if pagination is present.
        """
        products = response.css('ul#product-lister > li')

        for prod in products:
            prod_text = prod.css('p::text').get()
            url = response.meta["url"]
            prod_url = url + prod.css('a').attrib['href']
            prod_prix = prod.css('div._5d34bd7a ::text').get()
            cat = url[25:].split('/')
            unique = prod.css('a').attrib['href'].split('/')
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
            next_page_url = f"https://www.castorama.fr{next_page}"
            yield response.follow(next_page_url, callback=self.parse, meta={"url" : url})

        else:
            print("no more page")

