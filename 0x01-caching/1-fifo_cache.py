#!/usr/bin/env python3
"""
defines a class FIFOCache
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    caching system that inherits from BaseCaching
    """
    def __init__(self):
        """ class initializer """
        super().__init__()

    def put(self, key, item):
        """
        assigns the item value for the key 'key'
        to the dictionary 'self.cache_data' that is inherited
        from BaseCaching
        """
        if key is not None and item is not None:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_item = next(iter(self.cache_data))
                self.cache_data.pop(first_item)
                print("DISCARD: {}".format(first_item))
            self.cache_data[key] = item

    def get(self, key):
        """
        returns the value of self.cache_data that is linked to 'key'
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
