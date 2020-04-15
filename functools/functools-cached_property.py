"""Cached properties are similar to properties except that their value is cached after the first use"""

import time

import logging
import sys

FORMAT = "%(asctime)s %(levelname)s %(filename)s %(funcName)s %(lineno)s: %(message)s"
HANDLERS = (logging.StreamHandler(sys.stdout),)
logging.basicConfig(format=FORMAT, handlers=HANDLERS, level=logging.INFO)

from typing import Iterable, Callable
from functools import cached_property


class BigDataSet:
    def __init__(self, nums: Iterable[int], process: Callable[[Iterable[int]], int]):
        self._data = nums
        self._process = process

    @cached_property
    def processed_data(self) -> int:
        return self._process(self._data)


from itertools import count, takewhile, filterfalse
import timeit

if __name__ == '__main__':
    big_iterable = takewhile(lambda x: x < 100000000,
                             filterfalse(lambda x: x % 7 != 0, count(0)))
    set1 = BigDataSet(big_iterable, sum)
    start = time.perf_counter()
    logging.info("First call")
    set1.processed_data
    # * About 40 seconds
    logging.info(f"{time.perf_counter() - start}")
    start = time.perf_counter()
    set1.processed_data
    # * Much less than one second
    logging.info(f"{time.perf_counter() - start}")
