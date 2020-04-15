
import logging
import sys

FORMAT = "%(asctime)s %(levelname)s %(filename)s %(funcName)s %(lineno)s: %(message)s"
HANDLERS = (logging.StreamHandler(sys.stdout),)
logging.basicConfig(format=FORMAT, handlers=HANDLERS, level=logging.INFO)

from functools import lru_cache


# ! Prefer using powers of 2 for maxsize since they are optimised. If not set the maxsize is unlimited.
@lru_cache(maxsize=256)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


first_20_fib = [fib(n) for n in range(0, 20)]

logging.info(first_20_fib)
logging.info(fib.cache_info())
