import scrapy
from castorama.items import CastoramaItem

class CastospiderSpider(scrapy.Spider):
    name = "castospider2"
    allowed_domains = ["castorama.fr"]
    start_urls = ["https://www.castorama.fr/"]

    def parse(self, response: dict):
        """_summary_

        Args:
            response (_type_): _description_

        Yields:
            _type_: _description_
        """
        orig_url = "https://www.castorama.fr"
        product_categories = response.css('#megaNav-list\[1\] > li> a')
        
        for category in product_categories:
            cat_text = category.css('span::text').get()
            url_cat = orig_url + category.css('a').attrib['href']
            yield response.follow(url_cat, callback=self.parse_subcat, meta={"url_cat" : orig_url, "cat_text": cat_text})


    def parse_subcat(self, response):
        """_summary_

        Args:
            response (_type_): _description_

        Yields:
            _type_: _description_
        """
        url_cat = response.meta["url_cat"]
        my_sub_cat = response.css('ul#side-navigation-menu-1 > li > a ')
        my_sub_cat2 = response.css('div._6d8c96a3:nth-child(1) > div:nth-child(3) > a')

        if len(my_sub_cat) == 0 and len(my_sub_cat2) == 0:
            sub_cat = response.meta["sub_cat"]
            text = sub_cat[25:].split('/')
            if text[3][0:6] == 'cat_id':
                text[3] = text[2]
            unique = text[-1]
            yield {
                "category": text[3],
                "is_page_list": True,
                "url": sub_cat,
            }

        else:
            if len(my_sub_cat) == 0:
                my_sub_cat2 = response.css('div._6d8c96a3:nth-child(1) > div:nth-child(3) > a')
                for subcategory2 in my_sub_cat2:
                    url_sub_cat = url_cat + subcategory2.css('a').attrib['href']
                    sub_cat2_text = subcategory2.css('span::text').get()
                    yield {
                        "category" : sub_cat2_text,
                        "is_page_list": False,
                        "url": url_sub_cat,
                    }
                    yield response.follow(url_sub_cat, callback=self.parse_subcat, meta={"url_cat" : url_cat, "cat_text" : sub_cat_text, "sub_cat": url_sub_cat})
               
            if len(my_sub_cat2) == 0:
                for subcategory in my_sub_cat:
                    sub_cat_text = subcategory.css('::text').get()
                    url_sub_cat = url_cat + subcategory.css('a').attrib['href']
                    yield {
                        "category" : sub_cat_text,
                        "is_page_list": False,
                        "url": url_sub_cat,
                    }
                    yield response.follow(url_sub_cat, callback=self.parse_subcat, meta={"url_cat" : url_cat, "cat_text" : sub_cat_text, "sub_cat": url_sub_cat})
    