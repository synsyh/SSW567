"""
SSW567-HW01 by Yuning Sun
15:12 2020/1/28
Module documentation: 
"""

import math
import unittest


def classify_triangle(a, b, c):
    """
    Classify triangle
    @param a: length of one side
    @param b: length of one side
    @param c: length of one side
    @return: a string of types of triangle
    """
    if a == 0 or b == 0 or b == 0:
        raise ValueError('Please enter any numbers >0')
    if a + b + c <= max(a, b, c) * 2:
        raise ValueError('These 3 numbers can not make a triangle')
    result = ''
    if a == b and b == c:
        return 'Equilateral'
    elif a == b or b == c or a == c:
        result += 'Isosceles'
    m = max(a, b, c)
    if a ** 2 + b ** 2 + c ** 2 == m ** 2 * 2:
        result += 'Right'
    if result == '':
        result = 'Scalene'
    return result


def run_classify_triangle(a, b, c):
    # run classify triangle function and print the result
    print(classify_triangle(a, b, c))


class TestTriangles(unittest.TestCase):
    # Test function
    def test_case_1(self):
        # test equal situation
        self.assertEqual(classify_triangle(2, 3, 4), 'Scalene')
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral')
        self.assertEqual(classify_triangle(3, 4, 5), 'Right')
        self.assertEqual(classify_triangle(3, 3, 5), 'Isosceles')
        self.assertEqual(classify_triangle(math.sqrt(2), math.sqrt(2), 2), 'IsoscelesRight')

    def test_case_2(self):
        # test not equal situation
        self.assertNotEqual(classify_triangle(3, 4, 5), 'Scalene', 'It should be Right')

    def test_case_3(self):
        # test exceptions
        with self.assertRaises(ValueError):
            classify_triangle(1, 2, 3)
        with self.assertRaises(ValueError):
            classify_triangle(0, 2, 3)


if __name__ == '__main__':
    # main function to start testing
    # run_classify_triangle(2, 2, 5)
    unittest.main()
