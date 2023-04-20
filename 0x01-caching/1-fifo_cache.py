#!/usr/bin/env python3
"""
1. FIFO caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    A class FIFOCache that inherits from
    BaseCaching and is a caching system:
    """

    def __init__(self):
        """Constructor method"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Store a key-value pair
        """
        if key is None or item is None:
            pass
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded = self.order.pop(0)
            print("DISCARD: {}".format(discarded))
            del self.cache_data[discarded]
        self.order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Returns the value in self.cache_data associated with key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
