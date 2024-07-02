#!/usr/bin/env python3
"""
The basic cache module
"""
from typing import Any

BaseCache = __import__('base_caching').BaseCaching


class BasicCache(BaseCache):
    """
    Basic Caching class that uses py dict
    """

    def put(self, key: str, value: Any) -> None:
        """
        Put a value into the cache
        :param key: the key to store the value in
        :param value: the value to store
        """

        if key and value:
            self.cache_data[key] = value

    def get(self, key: str) -> None:
        """
        Print cached value
        """
        if key:
            if key in self.cache_data:
                return self.cache_data[key]

        return None
