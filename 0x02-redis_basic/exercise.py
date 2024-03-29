#!/usr/bin/env python3
"""interpreter used"""
import redis
import uuid
from typing import Union


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
