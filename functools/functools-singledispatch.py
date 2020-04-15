"""Singledispatch refers to generic methods were the actual implementation called depends on the type of the argument supplied. 
The singledispatch decorator can be used to create overidden generic functions."""

from itertools import chain
from functools import singledispatch


import logging
import sys

FORMAT = "%(asctime)s %(levelname)s %(filename)s %(funcName)s %(lineno)s: %(message)s"
HANDLERS = (logging.StreamHandler(sys.stdout),)
logging.basicConfig(format=FORMAT, handlers=HANDLERS, level=logging.INFO)


# ! The original function is registered for the type 'object' - usual MRO is used to determine which function to use.
@singledispatch
def concat(val1, val2):
    raise NotImplementedError(
        f"Concat cannot be performed on an object of type {type(val1)}")


@concat.register
def _(val1: int, val2: int):
    return val1 * 10 + val2


@concat.register
def _(val1: list, val2: list):
    return val1 + val2


@concat.register(str)  # ! Alternative to type annotation
def _(val1, val2):
    return ",".join([val1, val2])


logging.info(concat([1, 2, 3], [4, 5, 6]))  # * Prints [1,2,3,4,5,6]
logging.info(concat(1, 2))  # * Prints 12
logging.info(concat("a", "b"))  # * Prints a,b
logging.info(concat.registry.keys())

from functools import singledispatchmethod


class Keyer:
    @singledispatchmethod  # ! Must be outer wrapper
    def key(self, val):
        raise NotImplementedError('Cannot key a generic object.')

    @key.register
    def _(self, val: str):
        return val[-1]

    @key.register
    def _(self, val: int):
        return val % 10


# logging.info(Keyer.key(object())) # * Raises an error
keyer = Keyer()
logging.info(keyer.key('abcd'))  # * Prints d
logging.info(keyer.key(1234))  # * Prints 4
