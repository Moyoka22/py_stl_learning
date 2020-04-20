import unittest
from unittest import mock


class SomeClass:
    def __init__(self):
        self.a = "a"
        self.b = 2
        self.c = lambda x: x * 2


if __name__ == "__main__":
    instance = SomeClass()
    mock_obj = mock.Mock(spec=instance)
    mock_obj.a  # * no problem
    mock_obj.b  # * no problem
    mock_obj.c  # * no problem
    # mock_obj.d  # ! This will raise an AttributeError because SomeClass does not define an attribute 'd'
    mock_obj.e = 2  # * But setting is still allowed

    mock_obj2 = mock.Mock(
        spec_set=instance
    )  # * Spec only prevents getting, to also prevent setting use spec_set
    # mock_obj2.e = 2  # ! Now this is not allowed
