from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class CastoramaPipeline:
    """
    Processes items to ensure the 'subsubsubcategory' field is not equal to the 'unique_id' field.
    If both fields are equal, it resets 'subsubsubcategory' to an empty string.

    Args:
        item: The item being processed.
        spider: The spider that scraped the item.

    Returns:
        The processed item with updated fields if necessary.
    """
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        value = adapter.get("subsubsubcategory")
        value2 = adapter.get("unique_id")
        if value == value2:
            adapter["subsubsubcategory"] = ""
        return item

class ProductPipeline:
    """
    Processes items to check the 'subsubsubcategory' field for a specific prefix.
    If the field starts with 'cat_id', it resets 'subsubsubcategory' to an empty string.

    Args:
        item: The item being processed.
        spider: The spider that scraped the item.

    Returns:
        The processed item with updated fields if necessary.
    """
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        value = adapter.get("subsubsubcategory")

        if value[0][:6] == "cat_id":
            adapter["subsubsubcategory"] = ""
        return item
    
class OrderPipeline:
    """
    Processes items to extract specific order-related fields.

    Args:
        item: The item being processed.
        spider: The spider that scraped the item.

    Returns:
        A dictionary containing the extracted order fields.
    """
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        order_fields = ["unique_id","category","subcategory","subsubcategory","subsubsubcategory","title","price","url"]
        order_items = {field: adapter.get(field) for field in order_fields}
        return order_items

class DuplicatesPipeline:
    """
    Filters out duplicate items based on their 'unique_id' field.
    Maintains a set of seen IDs and drops any item with a duplicate ID.

    Args:
        item: The item being processed.
        spider: The spider that scraped the item.

    Returns:
        The item if its 'unique_id' has not been seen before.

    Raises:
        DropItem: If the item's 'unique_id' has already been processed.
    """
    def __init__(self):
        self.ids_seen = set()


    def process_item(self, item, spider):
        """
        Checks if the item's 'unique_id' has already been processed and drops duplicates.
        Adds new unique IDs to the set and returns the item if it is not a duplicate.

        Args:
            item: The item being processed.
            spider: The spider that scraped the item.

        Returns:
            The item if its 'unique_id' is not a duplicate.

        Raises:
            DropItem: If the item's 'unique_id' has already been processed.
        """
        adapter = ItemAdapter(item)

        if adapter["unique_id"] in self.ids_seen:
            raise DropItem(f"Item ID already seen: {adapter["unique_id"]}")

        self.ids_seen.add(adapter["unique_id"])
        return item