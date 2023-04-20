#!/usr/bin/env python3
"""
4. MRU Caching
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    A class MRUCache that inherits from
    BaseCaching and is a caching system:
    """

    def __init__(self):
        """
        Initialize the cache data
        """
        super().__init__()
        self.mru_key = None

    def put(self, key, item):
        """
        Store a key-value pair
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.mru_key = key
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                print(f"DISCARD: {self.mru_key}")
                del self.cache_data[self.mru_key]
            self.cache_data[key] = item
            self.mru_key = key

    def get(self, key):
        """
        Return the value that corresponds to the key in the cached data
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
