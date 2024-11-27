import scrapy


class ProductspiderSpider(scrapy.Spider):
    name = "productspider"
    allowed_domains = ["www.castorama.fr"]
    start_urls = ["https://www.castorama.fr/jardin-et-terrasse/cloture-panneau-grillage-brise-vue/panneau-a-composer-et-cloture-personnalisable/cloture-a-composer-pvc/cat_id_0001603.cat"]

    def parse(self, response):
        products = response.css('ul#product-lister > li')
        
        for prod in products:
            prod_text = prod.css('p::text').get()
            prod_url = "https://www.castorama.fr/jardin-et-terrasse/cloture-panneau-grillage-brise-vue/panneau-a-composer-et-cloture-personnalisable/cloture-a-composer-pvc/cat_id_0001603.cat" + prod.css('a').attrib['href']
            prod_prix = prod.css('div._5d34bd7a ::text').get()
            yield {
                "title" : prod_text,
                "prod_url" : prod_url,
                "prix" : prod_prix,
            }

