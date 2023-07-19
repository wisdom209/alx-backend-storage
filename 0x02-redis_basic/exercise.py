#!/usr/bin/env python3
"""writing strings to redis"""
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(fn: Callable) -> Callable:
    """count calls"""
    key = fn.__qualname__

    @wraps(fn)
    def wrapper(self, *args, **kwargs):
        """wrap decorated function"""
        self._redis.incr(key)
        return fn(self, *args, **kwargs)
    return wrapper

class Cache:
    """cache class"""

    def __init__(self):
        """initial function"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """a method that takes arg and returns a string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable]) -> Union[str, bytes, int, float]:
        """read from redis"""
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """parametrize cache.get"""
        value = self._redis.get(key)
        return value.decode('utf-8')

    def get_int(self, key: str) -> int:
        """parametrize cache.get"""
        value = self._redis.get(key)
        return value.decode('utf-8')
