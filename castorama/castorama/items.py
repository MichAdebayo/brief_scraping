import scrapy

class CastoramaItem(scrapy.Item):
    url = scrapy.Field()
    category = scrapy.Field()
    subcategory = scrapy.Field()
    subsubcategory = scrapy.Field()
    subsubsubcategory = scrapy.Field()
    unique_id = scrapy.Field()

class ProductItem(scrapy.Item):
    category = scrapy.Field()
    subcategory = scrapy.Field()
    subsubcategory = scrapy.Field()
    subsubsubcategory = scrapy.Field()
    unique_id = scrapy.Field()
    price = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    
