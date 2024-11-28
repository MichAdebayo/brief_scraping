# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CastoramaPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        value = adapter.get("subsubsubcategory")
        value2 = adapter.get("unique_id")
        if value == value2:
            adapter["subsubsubcategory"] = ""



        return item
