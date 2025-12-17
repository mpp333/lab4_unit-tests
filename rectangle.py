import unittest


def area(a, b):
    """
    Calculate the area of a rectangle.

    The area is calculated by multiplying the length of two adjacent sides.
    This function assumes both sides are positive numbers.

    Parameters:
    a (float): Length of the first side of the rectangle
    b (float): Length of the second side of the rectangle

    Returns:
    float: Area of the rectangle (a * b)

    Example:
    >>> area(5, 4)
    20
    >>> area(3.5, 2)
    7.0

    Raises:
    ValueError: If either side is negative (depends on implementation)
    """
    return a * b


def perimeter(a, b):
    """
    Calculate the perimeter of a rectangle.

    The perimeter is calculated by summing all four sides.
    Since opposite sides are equal, formula is 2*(a + b).

    Parameters:
    a (float): Length of the first side of the rectangle
    b (float): Length of the second side of the rectangle

    Returns:
    float: Perimeter of the rectangle (2*(a + b))

    Example:
    >>> perimeter(5, 4)
    18
    >>> perimeter(3.5, 2)
    11.0

    Raises:
    ValueError: If either side is negative (depends on implementation)
    """
    return 2 * (a + b)



class TestRectangle(unittest.TestCase):
    """Тесты для функций area и perimeter из модуля rectangle"""


    # --- Тесты для функции area() ---


    def test_area_normal_values(self):
        """Проверка площади для стандартных положительных значений"""

        self.assertEqual(area(5, 10), 50)
        self.assertEqual(area(3, 7), 21)

    def test_area_zero_values(self):
        """Проверка площади, если одна из сторон равна нулю"""

        self.assertEqual(area(10, 0), 0)
        self.assertEqual(area(0, 5), 0)

    def test_area_square(self):
        """Проверка площади квадрата (стороны равны)"""

        self.assertEqual(area(10, 10), 100)

    def test_area_negative_value_raises_error(self):
        """Проверка, что функция вызывает ValueError при отрицательной стороне"""

        with self.assertRaises(ValueError):
            area(-5, 10)
        with self.assertRaises(ValueError):
            area(5, -10)

    # --- Тесты для функции perimeter() ---


    def test_perimeter_normal_values(self):
        """Проверка периметра для стандартных положительных значений"""

        self.assertEqual(perimeter(5, 10), 30)
        self.assertEqual(perimeter(3, 7), 20)

    def test_perimeter_zero_values(self):
        """Проверка периметра, если одна из сторон равна нулю"""

        self.assertEqual(perimeter(10, 0), 20)
        self.assertEqual(perimeter(0, 5), 10)

    def test_perimeter_negative_value_raises_error(self):
        """Проверка, что функция вызывает ValueError при отрицательной стороне"""

        with self.assertRaises(ValueError):
            perimeter(-5, 10)


if __name__ == '__main__':
    unittest.main()
