#!/usr/bin/env python3
"""
defines a class LRUCache
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    least recently used caching system that inherits from
    BaseCaching
    """
    def __init__(self):
        """ init method """
        super().__init__()

    def put(self, key, item):
        """
        assigns 'item' value for the key 'key' to the dictionary
        'self.cache_data'
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lru = next(iter(self.cache_data))
            del self.cache_data[lru]
            print("DISCARD: {}".format(lru))

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            # Move the key to the end of the order_used list
            item = self.cache_data.pop(key)
            self.cache_data[key] = item
            return item
        return None
