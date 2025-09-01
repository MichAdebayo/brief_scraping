import scrapy

class CastoramaItem(scrapy.Item):
    """
    Represents a scraped item from the Castorama website.
    Stores various category fields, a unique identifier, and the item's URL.
    """
    url = scrapy.Field()
    category = scrapy.Field()
    subcategory = scrapy.Field()
    subsubcategory = scrapy.Field()
    subsubsubcategory = scrapy.Field()
    unique_id = scrapy.Field()

class ProductItem(scrapy.Item):
    """
    Represents a product item scraped from the Castorama website.
    Contains category information, product details, and a unique identifier.
    """
    category = scrapy.Field()
    subcategory = scrapy.Field()
    subsubcategory = scrapy.Field()
    subsubsubcategory = scrapy.Field()
    unique_id = scrapy.Field()
    price = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    