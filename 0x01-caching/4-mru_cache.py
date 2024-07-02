#!/usr/bin/env python3
"""
The module contains LRUCache class.
"""
from typing import Any

BaseCache = __import__('base_caching').BaseCaching


class MRUCache(BaseCache):
    """
    The fifo cache
    """

    def __init__(self):
        super().__init__()
        self.queue = []

    def put(self, key: str, item: Any) -> None:
        """
        Add an item in the cache
        """

        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            if len(self.queue) >= self.MAX_ITEMS:
                discarded = self.queue.pop(-1)
                del self.cache_data[discarded]
                print("DISCARD:", discarded)
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key: str) -> Any:
        """Get an item by key"""

        if key in self.queue:
            self.queue.remove(key)
            self.queue.append(key)

        return self.cache_data.get(key, None)
