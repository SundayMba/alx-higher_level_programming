import unittest
from models.base import Base

""" unittest module for Base class """

class TestBase(unittest.TestCase):

    def test_base1(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
    def test_base2(self):
        b2 = Base()
        self.assertEqual(b2.id, 2)
    def test_base3(self):
        b3 = Base()
        self.assertEqual(b3.id, 3)
    def test_base4(self):
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
    def test_base5(self):
        b5 = Base()
        self.assertEqual(b5.id, 4)


if __name__ == '__main__':
    unittest.main()
