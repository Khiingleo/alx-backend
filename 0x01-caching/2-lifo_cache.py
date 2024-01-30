#!/usr/bin/env python3
"""
defines a class LIFOCache
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    caching system that inherits from BaseCaching
    """
    def __init__(self):
        """ init method """
        super().__init__()

    def put(self, key, item):
        """
        assings 'item' value of the key 'key' to the
        dictionary self.cache_data(inherited from BaseCaching)
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            del self.cache_data[self.last_item]
            print("DISCARD: {}".format(self.last_item))

        if key in self.cache_data:
            self.last_item = key

    def get(self, key):
        """
        returns the value in self.cache_data linked to 'key'
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
