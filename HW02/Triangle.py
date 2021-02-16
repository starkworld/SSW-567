"""
Created on Tuesday 16 Feb 13:44:00 2021


The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: Nikhil Kalyan
"""


def classifyTriangle(a:int, b:int, c: int) -> str:
    """

    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'

      CAUTION: there may be a bug or two in this code
    """

    intersection: set = {a, b, c} & {a, b, c}
    is_right_triangle: bool = a ** 2 + b ** 2 == c ** 2
    triangle_class: str = 'Invalid Input values'

    # if values are invalid then return invalid input
    if a <= 0 or b <= 0 or c <= 0:
        return triangle_class

    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return triangle_class

    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a > b + c) or (b > a + c) or (c > a + b):
        return 'NotATriangle'

    # now we know that we have a valid triangle
    if is_right_triangle:
        triangle_classification: str = 'Right Angle Triangle'
    elif len(intersection) == 1:
        triangle_classification: str = 'Equilateral  Triangle'
    elif len(intersection) == 2:
        triangle_classification: str = 'Isosceles Triangle'
    else:
        triangle_classification: str = 'Scalene Triangle'

    return triangle_classification
