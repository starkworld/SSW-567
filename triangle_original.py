def classify_triangle(a, b, c):
    intersection = {a, b, c} & {a, b, c}
    is_right_triangle = a ** 2 + b ** 2 == c ** 2
    triangle_class = 'Invalid Input values'

    if a < 0 or b < 0 or c < 0:
        return triangle_class

    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return triangle_class

    if (a > b + c) or (b > a + c) or (c > a + b):
        return 'NotATriangle'

    if is_right_triangle:
        triangle_classification = 'Right Angle Triangle'
    elif len(intersection) == 1:
        triangle_classification = 'Equilateral  Triangle'
    elif len(intersection) == 2:
        triangle_classification = 'Isosceles Triangle'
    else:
        triangle_classification = 'Scalene Triangle'

    return triangle_classification
