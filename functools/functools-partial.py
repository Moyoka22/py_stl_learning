
import logging
import sys

FORMAT = "%(asctime)s %(levelname)s %(filename)s %(funcName)s %(lineno)s: %(message)s"
HANDLERS = (logging.StreamHandler(sys.stdout),)
logging.basicConfig(format=FORMAT, handlers=HANDLERS, level=logging.INFO)


def function_with_an_obnoxious_number_of_arguments(a, b, c, d, e, f, g, h, i, j, k, l, m, kwarg_a=None, kwarg_b=None, kwarg_c=None):
    res = a + b + c + d + e + f + g + h + i + j + k + l + m
    if kwarg_a:
        res += kwarg_a
    if kwarg_b:
        res += kwarg_b
    if kwarg_c:
        res += kwarg_c
    return res


from functools import partial

function_with_reasonable_argument_list = partial(
    function_with_an_obnoxious_number_of_arguments, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, kwarg_a=1, kwarg_b=2)

logging.info(function_with_reasonable_argument_list(13, kwarg_c=3))


# * Partial can also be used to create smaller functions with defaults defined

def add_numbers(x, y): return x + y


add_two = partial(add_numbers, 2)

logging.info(add_two(2))  # * Prints 4

base_two = partial(int, base=2)

logging.info(base_two('1000000'))  # * Prints 64

# ! Partialmethod performs the same as partial but for methods
from functools import partialmethod


class Counter:
    def __init__(self):
        self._count = 0

    @property
    def count(self):
        return self._count

    def _set_count(self, count):
        self._count = count

    def _add_to_count(self, value):
        self._count += value

    reset = partialmethod(_set_count, 0)
    increment = partialmethod(_add_to_count, 1)
    decrement = partialmethod(_add_to_count, -1)


counter1 = Counter()
counter1.increment()
counter1.increment()
logging.info(counter1.count)  # * Prints 2
counter1.reset()
logging.info(counter1.count)  # * Prints 0
