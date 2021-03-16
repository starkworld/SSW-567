
import unittest
from triangle_original import classify_triangle


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

    def test_classify_isosceles_triangles(self):
        """
        Testcases classify isosceles triangle
        """
        self.assertEqual(classify_triangle(65, 65, 130), 'Isosceles Triangle')

    def test_classify_scalene_triangle(self):
        """
        Testcases scalene triangle
        """
        self.assertEqual(classify_triangle(1, 2, 3), 'Scalene Triangle')

    def test_classify_right_triangles(self):
        """
        Testcases classify right triangle
        """
        self.assertEqual(classify_triangle(3, 4, 5), 'Right Angle Triangle')


if __name__ == '__main__':
    print('Unittest Running')
    unittest.main(exit=False, verbosity=2)
