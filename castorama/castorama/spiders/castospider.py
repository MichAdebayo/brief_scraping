import scrapy

class CastospiderSpider(scrapy.Spider):
    name = "castospider"
    allowed_domains = ["castorama.fr"]
    start_urls = ["https://www.castorama.fr/"]


    def parse(self, response):
        orig_url = "https://www.castorama.fr"
        product_categories = response.css('#megaNav-list\[1\] > li> a')
        category = product_categories[0]
        cat_text = category.css('span::text').get()
        url_cat = orig_url + category.css('a').attrib['href']
        yield response.follow(url_cat, callback=self.parse_subcat, meta={"url_cat" : orig_url, "cat_text": cat_text})


    def parse_subcat(self, response):
        url_cat = response.meta["url_cat"]
        my_sub_cat = response.css('ul#side-navigation-menu-1 > li > a ')
        my_sub_cat2 = response.css('div._6d8c96a3:nth-child(1) > div:nth-child(3) > a')

        if len(my_sub_cat) == 0 and len(my_sub_cat2) == 0:
            sub_cat = response.meta["sub_cat"]
            text = sub_cat[25:].split('/')
            yield {
                "category" : text[0],
                "url" : sub_cat,
            }

        elif len(my_sub_cat) == 0:
            my_sub_cat2 = response.css('div._6d8c96a3:nth-child(1) > div:nth-child(3) > a')
            for subcategory2 in my_sub_cat2:
                url_sub_cat = url_cat + subcategory2.css('a').attrib['href']
                sub_cat2_text = subcategory2.css('span::text').get()
                yield response.follow(url_sub_cat, callback=self.parse_subcat, meta={"url_cat" : url_cat, "cat_text" : sub_cat2_text, "sub_cat": url_sub_cat})

            # subcategory2 = my_sub_cat2[0]
            # url_sub_cat = url_cat + subcategory2.css('a').attrib['href']
            # sub_cat2_text = subcategory2.css('span::text').get()
            # yield response.follow(url_sub_cat, callback=self.parse_subcat, meta={"url_cat" : url_cat, "cat_text" : sub_cat2_text, "sub_cat": url_sub_cat})

        else:
            for subcategory in my_sub_cat:
                sub_cat_text = subcategory.css('::text').get()
                url_sub_cat = url_cat + subcategory.css('a').attrib['href']
                yield response.follow(url_sub_cat, callback=self.parse_subcat, meta={"url_cat" : url_cat, "cat_text" : sub_cat_text, "sub_cat": url_sub_cat})

    
            # subcategory = my_sub_cat[0]
            # sub_cat_text = subcategory.css('::text').get()
            # url_sub_cat = url_cat + subcategory.css('a').attrib['href']
            # yield response.follow(url_sub_cat, callback=self.parse_subcat, meta={"url_cat" : url_cat, "cat_text" : sub_cat_text, "sub_cat": url_sub_cat})

    