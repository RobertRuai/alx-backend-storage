#!/usr/bin/env python3
"""exercise module"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """returns a Callable"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """returns a Callable"""
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """wrapped function"""
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwds)
        self._redis.rpush(outputs, str(data))
        return data
    return wrapper


class Cache:
    """Cache class"""
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes data arg, generates random key,
        store data in redis with random key"""
        randkey = str(uuid.uuid4())
        self._redis.set(randkey, data)
        return randkey

    def get(
            self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """convert the data back to desired format"""
        res = self._redis.get(key)
        if (fn):
            return fn(res)
        return res

    def get_str(self, res: bytes) -> str:
        """convert result to string"""
        return str(res, 'UTF-8')

    def get_int(self, res: bytes) -> int:
        """convert result to int"""
        return int.from_bytes(res, "big")
