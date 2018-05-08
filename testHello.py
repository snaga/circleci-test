import unittest

from hello import hello, hello_pg

class TestHello(unittest.TestCase):
    def test_hello_001(self):
        self.assertEquals('hello', hello())

    def test_hello_pg_001(self):
        self.assertEquals('PostgreSQL 10', hello_pg()[:13])


if __name__ == '__main__':
    unittest.main()
