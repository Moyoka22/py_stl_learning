import unittest
from unittest import mock


class SomeClass:
    def __init__(self):
        self.a = "a"
        self.b = 2
        self.c = lambda x: x * 2


if __name__ == "__main__":
    instance = SomeClass()
    mock = mock.Mock(spec=instance)
    mock.a  # * no problem
    mock.b  # * no problem
    mock.c  # * no problem
    # mock.d  # ! This will raise an AttributeError because SomeClass does not define an attribute 'd'
