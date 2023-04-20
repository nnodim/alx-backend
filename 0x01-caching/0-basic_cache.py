#!/usr/bin/env python3
"""0. Basic dictionary
"""
BaseCaching = __import__('base_caching').BaseCaching
class BasicCache(BaseCaching):
    """
    A class BasicCache that inherits from BaseCaching and is a caching system:
    """

    def __init__(self):
        """Initialize the cache data"""
        super().__init__()

    def put(self, key, item):
        """
        Store a key-value pair
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value that corresponds to the key in the cached data
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
