from math import sqrt


class Node:
    def __init__(self, city_name, latitude, longitude, area=None):
        self.city_name = city_name
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.area = area

    def __str__(self):
        return self.city_name

    def get_distance(self, node):
        return sqrt((self.latitude - node.latitude) ** 2 +
                    (self.longitude - node.longitude) ** 2)
