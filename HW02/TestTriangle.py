from Triangle import classifyTriangle
import unittest


class TriangleClassification(unittest.TestCase):
    """
    Testing Classify triangle method
    Unittest class
    """

    def test_classify_equilateral_triangles(self):
        """
        Testcases for equilateral triangle
        """
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral  Triangle')
        self.assertEqual(classifyTriangle(10, 10, 10), 'Equilateral  Triangle')

    def test_classify_isosceles_triangles(self):
        """
        Testcases classify isosceles triangle
        """
        self.assertEqual(classifyTriangle(65, 65, 130), 'Isosceles Triangle')
        self.assertEqual(classifyTriangle(2, 3, 3), 'Isosceles Triangle')
        self.assertEqual(classifyTriangle(4, 6, 4), 'Isosceles Triangle')

    def test_classify_scalene_triangles(self):
        """
        Testcases scalene triangle
        """
        self.assertEqual(classifyTriangle(1, 2, 3), 'Scalene Triangle')
        self.assertEqual(classifyTriangle(7, 6, 3), 'Scalene Triangle')
        self.assertEqual(classifyTriangle(67, 87, 90), 'Scalene Triangle')

    def test_classify_right_triangles(self):
        """
        Testcases classify right triangle
        """
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right Angle Triangle')
        self.assertEqual(classifyTriangle(5, 12, 13), 'Right Angle Triangle')
        self.assertEqual(classifyTriangle(8, 15, 17), 'Right Angle Triangle')

    def test_classify_invalid_triangle(self):
        """
        Testcases classify
        """
        self.assertEqual(classifyTriangle(-10, -10, -10), 'Invalid Input values')
        self.assertEqual(classifyTriangle(201, 3, 1), 'NotATriangle')
        self.assertEqual(classifyTriangle(-1, 3, 1), 'Invalid Input values')
        self.assertEqual(classifyTriangle(1.5, 3, 1), 'Invalid Input values')
        self.assertEqual(classifyTriangle(1, 2, 10), 'NotATriangle')


if __name__ == '__main__':
    print('Unittest Running')
    unittest.main(exit=False, verbosity=2)
