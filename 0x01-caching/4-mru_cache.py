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
        self.queue = []

    def put(self, key, item):
        """
        Store a key-value pair
        """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.queue[-1]))
                del self.cache_data[self.queue[-1]]
                del self.queue[-1]
            if key in self.queue:
                del self.queue[self.queue.index(key)]
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value that corresponds to the key in the cached data
        """
        if key is not None and key in self.cache_data.keys():
            del self.queue[self.queue.index(key)]
            self.queue.append(key)
            return self.cache_data[key]
        return None
