#!/usr/bin/env python3
"""interpreter used."""
import redis
import uuid
from typing import Union, Optional, Callable
import functools


def replay(cache_method: Callable) -> None:
    """
    function that displays the history of calls of a particular function
    """
    input_key = cache_method.__qualname__ + ':inputs'
    output_key = cache_method.__qualname__ + ':outputs'

    print(cache_method.__qualname__ + ' was called {} times:'.format(
        cache_method.__self__._redis.get(cache_method.__qualname__).decode()))

    inputs_lst = cache_method.__self__._redis.lrange(input_key, 0, -1)
    outputs_lst = cache_method.__self__._redis.lrange(output_key, 0, -1)

    for inp, out in zip(inputs_lst, outputs_lst):
        print("{}(*{})".format(
            cache_method.__qualname__, eval(inp.decode())))


def call_history(method: Callable) -> Callable:
    """function to store the history of inpurt and outputs
    for a particular function"""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """method that wraps the original method"""
        input_arguments = f"{method.__qualname__}:inputs"
        output_arguments = f"{method.__qualname__}:outputs"
        self._redis.rpush(input_arguments, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_arguments, output)
        return output
    return wrapper


def count_calls(method: Callable) -> Callable:
    """function to use a decorator to count method
    calls"""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """function that wraps the original method"""
        key = method.__qualname__
        self._redis.incr(key)

        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """default cache class"""
    def __init__(self):
        """initialization of cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
