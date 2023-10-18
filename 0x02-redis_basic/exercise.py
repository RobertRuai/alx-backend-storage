#!/usr/bin/env python3
"""exercise module"""
import redis
import uuid


class Cache:
    """Cache class"""
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data) -> str:
        """takes data arg, generates random key,
        store data in redis with random key"""
        randkey = str(uuid.uuid4())
        if isinstance(data, (str, bytes, int, float)):
            self._redis.set(randkey, data)
            return randkey
