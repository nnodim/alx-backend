#!/usr/bin/env python3
"""
2. LIFO Caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    A class LIFOCache that inherits from
    BaseCaching and is a caching system
    """

    def __init__(self):
        """
        Initialize the cache data
        """
        super().__init__()

    def put(self, key, item):
        """Store a key-value pair"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-2]
            print(f"DISCARD: {last_key}")
            del self.cache_data[last_key]

    def get(self, key):
        """Returns the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
