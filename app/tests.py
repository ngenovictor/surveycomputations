from django.test import TestCase as DjangoTestCase
from unittest import TestCase as UnitTestCase
from .calculations import AreaCalculator


class CalculationsTestCase(UnitTestCase):

    def test_given_triangle_coordinates_with_coordinates_returns_correct_area(self):
        coordinates = [(4, 0), (0, 0), (0, 3)]
        area = AreaCalculator().area_with_coordinates(coordinates)
        self.assertEqual(6.0, area)

    def test_given_rectangle_coordinates_with_coordinates_returns_correct_area(self):
        coordinates = [(4, 0), (0, 0), (0, 3), (4, 3)]
        area = AreaCalculator().area_with_coordinates(coordinates)
        self.assertEqual(12.0, area)