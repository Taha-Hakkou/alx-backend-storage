#!/usr/bin/env python3
""" exercise """
import redis
import uuid
from typing import Union, Callable, Optional, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ count_calls decorator """
    @wraps(method)
    def incrementer(self: Any, *args,
                    **kwargs) -> Union[str | bytes | int | float]:
        """ increments the calls count """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return incrementer


def call_history(function: Callable) -> Callable:
    """ call_history decorator """
    @wraps(function)
    def wrapper(self: Any, *args) -> str:
        self._redis.rpush(f'{function.__qualname__}:inputs', str(args))
        output = function(self, *args)
        self._redis.rpush(f'{function.__qualname__}:outputs', output)
        return output
    return wrapper


def replay(fn: Callable) -> None:
    """ displays the history of calls of a particular function """
    client = redis.Redis()
    calls = client.get(fn.__qualname__).decode('utf-8')
    inputs = [input.decode('utf-8') for input in
              client.lrange(f'{fn.__qualname__}:inputs', 0, -1)]
    outputs = [output.decode('utf-8') for output in
               client.lrange(f'{fn.__qualname__}:outputs', 0, -1)]
    print(f'{fn.__qualname__} was called {calls} times:')
    for input, output in zip(inputs, outputs):
        print(f'{fn.__qualname__}(*{input}) -> {output}')


class Cache:
    """ Cache class """
    def __init__(self: Any):
        """ creates a redis cache client """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str | bytes | int | float]) -> str:
        """ stores data in cache, and returns its key """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self: Any, key: str,
            fn: Optional[Callable] = None) -> Union[str | bytes | int | float]:
        """ returns data in the desired format """
        value = self._redis.get(key)
        if not value:
            return
        elif fn is int:
            return self.get_int(value)
        elif fn is str:
            return self.get_str(value)
        elif callable(fn):
            return fn(value)
        return value

    def get_str(self: Any, data: bytes) -> str:
        """ converts bytes into string """
        return data.decode('utf-8')

    def get_int(self: Any, data: bytes) -> int:
        """ converts bytes into int """
        return int(data)
