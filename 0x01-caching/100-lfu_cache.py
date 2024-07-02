#!/usr/bin/env python3
"""
The module contains LFU Cache class.
"""
from typing import Any

BaseCache = __import__('base_caching').BaseCaching


class LFUCache(BaseCache):
    """
    The LFU cache
    """

    def __init__(self):
        super().__init__()
        self.queue = {}

    def put(self, key: str, item: Any) -> None:
        """
        Add an item in the cache
        """
        if key and item:
            if key in self.cache_data:
                self.queue[key] += 1
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    least_accessed = min(self.queue.values())
                    for k, v in list(self.queue.items()):
                        if v == least_accessed:
                            del self.queue[k]
                            del self.cache_data[k]
                            print("DISCARD:", k)
                            break
                self.cache_data[key] = item
                self.queue[key] = 1

    def get(self, key: str) -> Any:
        """Get an item by key"""
        if key in self.cache_data:
            self.queue[key] += 1
            return self.cache_data[key]
        return None
