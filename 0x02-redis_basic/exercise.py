#!/usr/bin/env python3
"""exercise module"""
import redis
import uuid
from typing import Union


class Cache:
    """Cache class"""
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes data arg, generates random key,
        store data in redis with random key"""
        randkey = str(uuid.uuid4())
        self._redis.set(randkey, data)
        return randkey
