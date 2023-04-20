#!/usr/bin/env python3
"""
3. LRU Caching
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    A class LRUCache that inherits from
    BaseCaching and is a caching system:
    """

    def __init__(self):
        """
        Initialize the cache data
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        Store a key-value pair
        """
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                discarded = self.queue.pop(0)
                print(f"DISCARD: {discarded}")
                del self.cache_data[discarded]
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value in self.cache_data linked to key
        """
        if key and key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data[key]
        return None
