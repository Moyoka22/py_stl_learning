"""Allows decorators to work more smoothly by updating the function metadata to match the function being wrapped.
Metadata includes function """


import logging
import sys

FORMAT = "%(asctime)s %(levelname)s %(filename)s %(funcName)s %(lineno)s: %(message)s"
HANDLERS = (logging.StreamHandler(sys.stdout),)
logging.basicConfig(format=FORMAT, handlers=HANDLERS, level=logging.INFO)

from functools import wraps


def inspect_args(f):
    @wraps(f)  # * The outer definition accepts the wrapped function and allows the calling of the wraps decorator
    # * The inner function is what is invoked and it has its metadata updated
    def wrapper(*args, **kwargs):
        logging.info(
            f"Calling the function {f.__name__} with args {args} and kwargs {kwargs}")
        return f(*args, **kwargs)
    return wrapper


@inspect_args
def f(a, b, c):
    return a + b + c


f(1, 2, 3)
