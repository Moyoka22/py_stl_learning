import some_module
import unittest
from unittest import mock


class TestCaseOne(unittest.TestCase):
    @mock.patch("some_module.json")
    def test_json_load(self, mock_json):  # * Argument is the patched object
        o = mock.Mock()
        o.ttl = 1500.0
        mock_json.loads.return_value = o
        self.assertEqual(some_module.some_function("test"), 1500.0)

    def test_load_json_again(self):
        with mock.patch(
            "some_module.json"
        ) as mock_json:  # * Can also use a context manager instead of a decorator
            o = mock.Mock()
            o.ttl = 1500.0
            mock_json.loads.return_value = o
            self.assertEqual(some_module.some_function("test"), 1500.0)

    from some_module import (
        json,
    )  # * This import is needed to perform the patch successfully

    @mock.patch.object(json, "loads", return_value=mock.Mock(ttl=1500.0))
    def test_load_json_again_again(self, mock_json):
        self.assertEqual(some_module.some_function("test"), 1500.0)


if __name__ == "__main__":
    unittest.main()
