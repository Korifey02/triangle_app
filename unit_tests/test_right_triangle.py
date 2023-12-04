import unittest

from main.utils.triangle import RightTriangle


class TestRightTriangle(unittest.TestCase):

    def setUp(self):
        self.triangle1 = RightTriangle(3, 4)
        self.triangle2 = RightTriangle(5, 12)

    def test_get_first_side(self):
        self.assertEqual(self.triangle1.get_first_side(), 3)
        self.assertEqual(self.triangle2.get_first_side(), 5)

    def test_get_second_side(self):
        self.assertEqual(self.triangle1.get_second_side(), 4)
        self.assertEqual(self.triangle2.get_second_side(), 12)

    def test_hypotenuse(self):
        self.assertEqual(self.triangle1.hypotenuse, 5)
        self.assertEqual(self.triangle2.hypotenuse, 13)

    def test_area(self):
        self.assertEqual(self.triangle1.area, 6)
        self.assertEqual(self.triangle2.area, 30)

    def test_perimeter(self):
        self.assertEqual(self.triangle1.perimeter, 12)
        self.assertEqual(self.triangle2.perimeter, 30)

    def test_str(self):
        self.assertEqual(str(self.triangle1), 'A=3 B=4 C=5.0')
        self.assertEqual(str(self.triangle2), 'A=5 B=12 C=13.0')
