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
        self.usage = []
