#!/usr/bin/env python3
"""
defines a class BasicCache
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    a caching system that inherits from BaseCaching
    """
    def put(self, key, item):
        """
        assings to the dictionary
        self.cache_data(inherited from BaseCaching)
        the 'item' for the 'key'.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        returns the value of self.cache_data that is linked
        to key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
