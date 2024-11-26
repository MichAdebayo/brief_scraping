import scrapy

class CastospiderSpider(scrapy.Spider):
    name = "castospider"
    allowed_domains = ["castorama.fr"]
    start_urls = ["https://castorama.fr/"]


    def parse(self, response):
        orig_url = "https://castorama.fr"
        product_categories = response.css('#megaNav-list\[1\] > li> a')
        category = product_categories[0]
        cat_text = category.css('span::text').get()
        url_cat = orig_url + category.css('a').attrib['href']
        yield response.follow(url_cat, callback=self.parse_subcat, meta={"url_cat" : orig_url, "cat_text": cat_text})


    def parse_subcat(self, response):
        url_cat = response.meta["url_cat"]
        my_dict = {}
        cat_text = response.meta["cat_text"]
        my_sub_cat = response.css('ul#side-navigation-menu-1 > li > a ')
        subcategory = my_sub_cat[0]
        sub_cat_text = subcategory.css('span::text').get()
        if subcategory is None:
            print('no more cat')
        else:
            url_sub_cat = url_cat + subcategory.css('a').attrib['href']
            print(url_sub_cat)
            print(sub_cat_text)
            # my_dict[cat_text] = sub_cat_text
            # print(my_dict)
            yield response.follow(url_sub_cat, callback=self.parse_subcat, meta={"url_cat" : url_cat})
