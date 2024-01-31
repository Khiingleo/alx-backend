#!/usr/bin/env python3
"""
defines a class LFUCache
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    least frequently used caching system that inherits from
    BaseCaching
    """
    def __init__(self):
        """ init method """
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """
        assigns 'item' value for the key 'key' to the dictionary
        'self.cache_data'
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.frequency[key] += 1
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    discarded = min(self.frequency, key=self.frequency.get)
                    del self.cache_data[discarded]
                    del self.frequency[discarded]
                    print("DISCARD: {}".format(discarded))

                self.cache_data[key] = item
                self.frequency[key] = 0

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
