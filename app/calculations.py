class AreaCalculator(object):
    """
    This will contain all methods to compute area of parcels based on various factors
    """
    def area_with_coordinates(self, coordinates):
        """
        Given a set of coordinates return area
        :param coordinates:
        :return area:
        """
        area = 0
        x_points = []
        y_points = []

        j = len(coordinates) - 1

        for coordinate_points in coordinates:
            x_points.append(coordinate_points[0])
            y_points.append(coordinate_points[1])

        for i in range(len(coordinates)):
            area = area + (x_points[j]+x_points[i]) * (y_points[j]-y_points[i])
            j = i

        return area/2