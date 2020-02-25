"""
SSW567-HW01 by Yuning Sun
15:12 2020/1/28
Module documentation:
"""
import math
import unittest


def classify_triangle(length1, length2, length3):
    """
    Classify triangle
    @param length1: length of one side
    @param length2: length of one side
    @param length3: length of one side
    @return: a string of types of triangle
    """
    if length1 <= 0 or length2 <= 0 or length2 <= 0:
        raise ValueError('Please enter any numbers >0')
    if max(length1, length2, length3) * 2 >= length1 + length2 + length3:
        raise ValueError('These 3 numbers can not make a triangle')
    result = ''
    if length1 == length2 and length2 == length3:
        return 'Equilateral'
    elif length1 == length2 or length2 == length3 or length1 == length3:
        result += 'Isosceles'
    max_length = max(length1, length2, length3)
    if length1 ** 2 + length2 ** 2 + length3 ** 2 == max_length ** 2 * 2:
        result += 'Right'
    if result == '':
        result = 'Scalene'
    return result


class TestTriangles(unittest.TestCase):
    """
    Test function
    """

    def test_case_1(self):
        """
        test equal situation
        @return: None
        """
        self.assertEqual(classify_triangle(2, 3, 4), 'Scalene')
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral')
        self.assertEqual(classify_triangle(3, 4, 5), 'Right')
        self.assertEqual(classify_triangle(3, 3, 5), 'Isosceles')
        self.assertEqual(classify_triangle(math.sqrt(2), math.sqrt(2), 2), 'IsoscelesRight')

    def test_case_2(self):
        """
        test not equal situation
        @return: None
        """
        self.assertNotEqual(classify_triangle(3, 4, 5), 'Scalene', 'It should be Right')

    def test_case_3(self):
        """
        test exceptions
        @return: None
        """
        with self.assertRaises(ValueError):
            classify_triangle(1, 2, 3)
        with self.assertRaises(ValueError):
            classify_triangle(0, 2, 3)


if __name__ == '__main__':
    # main function to start testing
    # run_classify_triangle(2, 2, 5)
    unittest.main()
