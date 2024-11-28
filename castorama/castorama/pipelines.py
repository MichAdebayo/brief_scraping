# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class CastoramaPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        value = adapter.get("subsubsubcategory")
        value2 = adapter.get("unique_id")
        if value == value2:
            adapter["subsubsubcategory"] = ""

        return item

class ProductPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)
        order_fields = ["unique_id","category","subcategory","subsubcategory","subsubsubcategory","title","price","url"]
        order_items = {field: adapter.get(field) for field in order_fields}
        value = adapter.get("subsubsubcategory")
        if value[0][:6] == "cat_id":
            adapter["subsubsubcategory"] = ""

        return order_items

class DuplicatesPipeline:
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter["unique_id"] in self.ids_seen:
            raise DropItem(f"Item ID already seen: {adapter["unique_id"]}")
        else:
            self.ids_seen.add(adapter["unique_id"])
            return item