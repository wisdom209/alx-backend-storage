#!/usr/bin/env python3
"""writing strings to redis"""
import redis
import uuid
from typing import Union


class Cache:
    """cache class"""
    def __init__(self):
        """initial function"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, float, bytes, int]) -> str:
        """a method that takes arg and returns a string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
