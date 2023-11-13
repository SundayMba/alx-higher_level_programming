import unittest
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch


class TestRectangle(unittest.TestCase):

    def test_width_property1(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 12)
    def test_width_property2(self):
        with self.assertRaises(TypeError):
            r2 = Rectangle('3', 32)
    def test_width_property3(self):
        with self.assertRaises(ValueError):
            r3 = Rectangle(2, 4)
            r3.width = -2
    def test_width_property4(self):
        with self.assertRaises(TypeError):
            r4 = Rectangle(23, 9)
            r4.width = '3'
    def test_height_property1(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(23, 0)
    def test_height_property2(self):
        with self.assertRaises(TypeError):
            r2 = Rectangle(4, '3')
    def test_height_property3(self):
        with self.assertRaises(ValueError):
            r3 = Rectangle(2, 4)
            r3.height = -2
    def test_height_property4(self):
        with self.assertRaises(TypeError):
            r4 = Rectangle(23, 9)
            r4.height = '3'
    def test_x_property1(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(23, 12, -2)
    def test_x_property2(self):
        with self.assertRaises(TypeError):
            r2 = Rectangle(4, 32, '2')
    def test_x_property3(self):
        with self.assertRaises(ValueError):
            r3 = Rectangle(2, 4)
            r3.x = -4
    def test_x_property4(self):
        with self.assertRaises(TypeError):
            r4 = Rectangle(23, 9)
            r4.x = '3'
    def test_y_property1(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(4, 12, 3, -4)
    def test_y_property2(self):
        with self.assertRaises(TypeError):
            r2 = Rectangle(5, 32, 9, '3')
    def test_y_property3(self):
        with self.assertRaises(ValueError):
            r3 = Rectangle(2, 4)
            r3.y = -2
    def test_y_property4(self):
        with self.assertRaises(TypeError):
            r4 = Rectangle(23, 9)
            r4.y = '3'
    def test_area1(self):
        r = Rectangle(2, 4)
        self.assertEqual(r.area(), 8)
    def test_area2(self):
        r = Rectangle(2, 20)
        self.assertEqual(r.area(), 40)
    def test_area3(self):
        r = Rectangle(8, 7, 2, 8, 12)
        self.assertEqual(r.area(), 56)
    def test_area4(self):
        r = Rectangle(100, 200)
        self.assertEqual(r.area(), 20000)
    def test_area5(self):
        r = Rectangle(23, 100)
        self.assertEqual(r.area(), 2300)
    @patch('sys.stdout', new_callable=StringIO)
    def test_display1(self, mock_stdout):
        r = Rectangle(2, 2)
        r.display()
        d = "##\n##\n"
        self.assertEqual(mock_stdout.getvalue(), d)
    @patch('sys.stdout', new_callable=StringIO)
    def test_display2(self, mock_stdout):
        r = Rectangle(4, 6)
        r.display()
        d = """####\n####\n####\n####\n####\n####\n"""
        self.assertEqual(mock_stdout.getvalue(), d)

    @patch('sys.stdout', new_callable=StringIO)
    def test__str__1(self, mock_stdout):
        r1 = Rectangle(4, 6, 2, 1, 12)
        print(r1)
        self.assertEqual(mock_stdout.getvalue(), "[Rectangle] (12) 2/1 - 4/6\n")
    @patch('sys.stdout', new_callable=StringIO)
    def test__str__2(self, mock_stdout):
        r1 = Rectangle(5, 5, 1)
        print(r1)
        self.assertEqual(mock_stdout.getvalue(), "[Rectangle] (1) 1/0 - 5/5\n")





if __name__ == '__main__':
    unittest.main()
