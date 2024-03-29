#!/usr/bin/env python3
"""interpreter used"""
import redis
import uuid
from typing import Union, Optional, Callable


class Cache:
    """default cache class"""
    def __init__(self):
        """initialization of cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """method that takes data of any type as an argument
        and returns a string"""
        r_key = str(uuid.uuid4())
        self._redis.set(r_key, data)
        return r_key

    def get(self, key: str, fn:
            Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """method that take a key string argument
        and an optional Callable argument named fn"""
        new_data = self._redis.get(key)
        if new_data is None:
            return None
        if fn is not None:
            return fn(new_data)
        return new_data

    def get_str(self, key: str) -> str:
        """function that retrieves string data from cache"""
        return self._redis.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """function that retrieve integer data from cache"""
        return self._redis.get(key, fn=int)
