#!/usr/bin/env python3
"""
defines a class MRUCache
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Most recently used caching system that inherits from
    BaseCaching
    """
    def __init__(self):
        """ init method """
        super().__init__()
        self.most_recently_used = None

    def put(self, key, item):
        """
        assigns 'item' value for the key 'key' to the dictionary
        'self.cache_data'
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            mru = self.most_recently_used
            del self.cache_data[mru]
            print("DISCARD: {}".format(mru))

        if key in self.cache_data:
            self.most_recently_used = key

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            # Move the key to the end of the order_used list
            item = self.cache_data.pop(key)
            self.cache_data[key] = item
            self.most_recently_used = key
            return item
        return None
