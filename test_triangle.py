"""Unittesting for triangle program
    Author: Nikhil Kalyan
    Updated: 03/16/2021
"""

import unittest
from triangle import classify_triangle


class TestTriangle(unittest.TestCase):
    """
    Testing Classify triangle method
    Unittest class
    """

    def test_classify_equilateral_triangles(self):
        """
        Testcases for equilateral triangle
        """
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral  Triangle')
        self.assertEqual(classify_triangle(10, 10, 10), 'Equilateral  Triangle')

    def test_classify_isosceles_triangles(self):
        """
        Testcases classify isosceles triangle
        """
        self.assertEqual(classify_triangle(65, 65, 130), 'Isosceles Triangle')
        self.assertEqual(classify_triangle(2, 3, 3), 'Isosceles Triangle')
        self.assertEqual(classify_triangle(4, 6, 4), 'Isosceles Triangle')

    def test_classify_scalene_triangle(self):
        """
        Testcases scalene triangle
        """
        self.assertEqual(classify_triangle(1, 2, 3), 'Scalene Triangle')
        self.assertEqual(classify_triangle(7, 6, 3), 'Scalene Triangle')
        self.assertEqual(classify_triangle(67, 87, 90), 'Scalene Triangle')

    def test_classify_right_triangles(self):
        """
        Testcases classify right triangle
        """
        self.assertEqual(classify_triangle(3, 4, 5), 'Right Angle Triangle')
        self.assertEqual(classify_triangle(5, 12, 13), 'Right Angle Triangle')
        self.assertEqual(classify_triangle(8, 15, 17), 'Right Angle Triangle')

    def test_classify_invalid_triangle(self):
        """
        Testcases classify
        """
        self.assertEqual(classify_triangle(-10, -10, -10), 'Invalid Input values')
        self.assertEqual(classify_triangle(201, 3, 1), 'NotATriangle')
        self.assertEqual(classify_triangle(-1, 3, 1), 'Invalid Input values')
        self.assertEqual(classify_triangle(1.5, 3, 1), 'Invalid Input values')


if __name__ == '__main__':
    print('Unittest Running')
    unittest.main(exit=False, verbosity=2)
