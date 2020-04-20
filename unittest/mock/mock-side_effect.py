import unittest

from unittest.mock import Mock

some_package = Mock()


def do_something():
    return some_package.some_method()


class TestCaseOne(unittest.TestCase):
    def test_what_happens(self):
        # * The side_effect will be instantiated when the method is called
        some_package.some_method.side_effect = Exception
        with self.assertRaises(Exception):
            do_something()

    def test_what_happens_a_few_times(self):
        # * Supplying an iterator will cycle through the values as the return type; if an Exception is supplied, it will be raised.
        some_package.some_method.side_effect = [1, 2, Exception]
        do_something()
        do_something()
        with self.assertRaises(Exception):
            do_something()


if __name__ == '__main__':
    unittest.main()
