from django.test import TestCase as DjangoTestCase
from unittest import TestCase as UnitTestCase
from .calculations import AreaCalculator


class AreaCalculationsTestCase(UnitTestCase):

    def test_given_triangle_coordinates_with_coordinates_returns_correct_area(self):
        coordinates = [(4, 0), (0, 0), (0, 3)]
        area = AreaCalculator().area_with_coordinates(coordinates,1)
        self.assertEqual(6.0, area)

    def test_given_rectangle_coordinates_with_coordinates_returns_correct_area(self):
        coordinates = [(4, 0), (0, 0), (0, 3), (4, 3)]
        area = AreaCalculator().area_with_coordinates(coordinates,1)
        self.assertEqual(12.0, area)

    def test_given_actual_world_coordinated_returns_correct_area(self):
        coordinates = [(780481.558601328, 9934959.79893969), (781076.259852303, 9920686.96891631), (767228.21643676, 9920092.26766534), (766803.429828921, 9933260.65250834)]
        area = AreaCalculator().area_with_coordinates(coordinates,8)
        self.assertEqual(189422538.83016014, area)

    def test_given_actual_world_coordinated_returns_correct_area_with_defined_precision(self):
        coordinates = [(780481.558601328, 9934959.79893969), (781076.259852303, 9920686.96891631), (767228.21643676, 9920092.26766534), (766803.429828921, 9933260.65250834)]
        area = AreaCalculator().area_with_coordinates(coordinates, 2)
        self.assertEqual(189422538.83, area)

    def test_given_actual_world_coordinated_returns_correct_area_with_zero_precision(self):
        coordinates = [(780481.558601328, 9934959.79893969), (781076.259852303, 9920686.96891631), (767228.21643676, 9920092.26766534), (766803.429828921, 9933260.65250834)]
        area = AreaCalculator().area_with_coordinates(coordinates, 0)
        self.assertEqual(189422539, area)