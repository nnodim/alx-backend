#!/usr/bin/env python3
"""
5. LFU Caching
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    A class LFUCache that inherits from
    BaseCaching and is a caching system
    """

    def __init__(self):
        """
        Initialize the cache data
        """
        super().__init__()
        self.usage = []
        self.frequency = {}

    def put(self, key, item):
        """
        Store a key-value pair
        """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                lfu = min(self.frequency.values())
                lfu_keys = []
                for x, y in self.frequency.items():
                    if y == lfu:
                        lfu_keys.append(x)
                if len(lfu_keys) > 1:
                    lru_lfu = {}
                    for x in lfu_keys:
                        lru_lfu[x] = self.usage.index(x)
                    discard = min(lru_lfu.values())
                    discard = self.usage[discard]
                else:
                    discard = lfu_keys[0]

                print("DISCARD: {}".format(discard))
                del self.cache_data[discard]
                del self.usage[self.usage.index(discard)]
                del self.frequency[discard]
            if key in self.frequency:
                self.frequency[key] += 1
            else:
                self.frequency[key] = 1
            if key in self.usage:
                del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value that corresponds to the key in the cached data
        """
        if key is not None and key in self.cache_data.keys():
            del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
