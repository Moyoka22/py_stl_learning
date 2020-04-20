
import unittest

from unittest.mock import Mock

requests = Mock()
d = {'key': 'value'}
res = Mock()
res.json.return_value = d
requests.get.return_value = res


def make_get_request(url):
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    return None

class TestRequest(unittest.TestCase):

    def test_get_request(self):
        res.status_code = 200
        j = make_get_request("test")
        self.assertTrue(j['key'] == 'value')

    def test_get_bad_request(self):
        res.status_code = 400
        j = make_get_request("test")
        # * call_arg_list holds the arguments a method was called with for all calls
        self.assertTrue(res.json.call_args_list == [])
        # * call_args holds just the last call
        self.assertIsNone(res.json.call_args)
        # * Holds the number of times the method was called
        self.assertEqual(res.json.call_count, 1)
        self.assertIsNone(j)


if __name__ == '__main__':
    unittest.main()
