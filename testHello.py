import unittest

from hello import hello

class TestHello(unittest.TestCase):
    def test_hello_001(self):
        self.assertEquals('hello', hello())


if __name__ == '__main__':
    unittest.main()
