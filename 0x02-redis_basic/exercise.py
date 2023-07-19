#!/usr/bin/env python3
"""writing strings to redis"""
import redis
import uuid
from typing import Union, Optional, Callable


class Cache:
    """cache class"""

    def __init__(self):
        """initial function"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """a method that takes arg and returns a string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable]) -> Union[str, bytes, int, float]:
        """read from redis"""
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """parametrize cache.get"""
        value = self.get(key)
        return value.decode('utf-8')

    def get_int(self, key: str) -> int:
        """parametrize cache.get"""
        value = self.get(key)
        try:
            return int(value.decode('utf-8'))
        except Exception:
            return 0
