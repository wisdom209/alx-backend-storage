#!/usr/bin/env python3
"""writing strings to redis"""
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def replay(fn: Callable):
    '''display the history of calls of a particular function.'''
    r = redis.Redis()
    func_name = fn.__qualname__
    c = r.get(func_name)
    try:
        c = int(c.decode("utf-8"))
    except Exception:
        c = 0
    print("{} was called {} times:".format(func_name, c))
    inputs = r.lrange("{}:inputs".format(func_name), 0, -1)
    outputs = r.lrange("{}:outputs".format(func_name), 0, -1)
    for inp, outp in zip(inputs, outputs):
        try:
            inp = inp.decode("utf-8")
        except Exception:
            inp = ""
        try:
            outp = outp.decode("utf-8")
        except Exception:
            outp = ""
        print("{}(*{}) -> {}".format(func_name, inp, outp))
        
def count_calls(fn: Callable) -> Callable:
    """count calls"""
    key = fn.__qualname__

    @wraps(fn)
    def wrapper(self, *args, **kwargs):
        """wrap decorated function"""
        self._redis.incr(key)
        return fn(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    '''store the history of inputs and outputs for a particular function'''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''wrap the decorated function and return the wrapper'''
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)
        return output
    return wrapper


class Cache:
    """cache class"""

    def __init__(self):
        """initial function"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """a method that takes arg and returns a string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable]=None) -> Union[str, bytes, int, float]:
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
