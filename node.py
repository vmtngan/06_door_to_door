from math import sqrt
from sys import stderr


class Node:
    def __init__(self, city_name, latitude, longitude, area=None):
        self.city_name = city_name
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.area = area
        if not self.is_valid_coordinate():
            stderr.write('Invalid file\n')
            exit(1)

    def get_distance(self, node):
        return sqrt((self.latitude - node.latitude) ** 2 +
                    (self.longitude - node.longitude) ** 2)

    def is_valid_coordinate(self):
        return abs(self.latitude) <= 180 and abs(self.longitude) <= 180
