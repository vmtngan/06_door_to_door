from math import sqrt
from sys import stderr


class Node:
    """Represent a city in the map."""
    def __init__(self, city_name, latitude, longitude, area=(0, 0)):
        """
        Initialize attributes of the Node class.
        @param city_name: name of the city
        @param latitude: location of the city by latitude
        @param longitude: location of the city by longitude
        @param area: area address that contains the city
        """
        self.city_name = city_name
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.area = area
        # Check the longitude and latitude are valid
        if not self.is_valid_coordinate():
            stderr.write('Invalid file\n')
            exit(1)

    def get_distance(self, other_node):
        """
        Calculate distance between current city and another city.
        @param other_node: another city
        @return: distance between two cities
        """
        return sqrt((self.latitude - other_node.latitude) ** 2 +
                    (self.longitude - other_node.longitude) ** 2)

    def is_valid_coordinate(self):
        """
        Check the longitude and latitude are valid.
        @return: True - valid
                 False - invalid
        """
        return abs(self.latitude) <= 180 and abs(self.longitude) <= 180
