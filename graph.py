from abc import ABC, abstractmethod


class Graph(ABC):
    def __init__(self, node_list):
        self.node_list = node_list
        self.route = []
        self.total_distance = 0
        self.latitude_list = [node.latitude for node in self.node_list]
        self.longitude_list = [node.longitude for node in self.node_list]
        self.min_x = min(self.latitude_list)
        self.max_x = max(self.latitude_list)
        self.min_y = min(self.longitude_list)
        self.max_y = max(self.longitude_list)
        self.div_num = 350
        self.unit_x = self.unit_y = (self.max_x - self.min_x) / self.div_num
        self.area_list = self.split_graph()

    def split_graph(self):
        area_list = {}
        for node in self.node_list:
            node.area = (int(node.latitude // self.unit_x),
                         int(node.longitude // self.unit_y))
            if node.area in area_list:
                area_list[node.area].append(node)
            else:
                area_list[node.area] = [node]
        return area_list

    def __str__(self):
        return ' -> '.join([node.city_name for node in self.route])

    @abstractmethod
    def find_shortest_path(self):
        return