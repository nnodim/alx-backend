#!/usr/bin/env python3
"""
1. FIFO caching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    A class FIFOCache that inherits from
    BaseCaching and is a caching system:
    """

    def __init__(self):
        """initialize"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        Store a key-value pair
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.queue.remove(key)
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self.queue[0]))
                del self.cache_data[self.queue[0]]
                del self.queue[0]
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Returns the value in self.cache_data associated with key"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
