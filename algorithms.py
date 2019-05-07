from itertools import permutations
from graph import Graph


class BruteForce(Graph):
    def find_shortest_path(self):
        return self.route


class NearestNeighbor(Graph):
    def find_nearest_node(self, start_node, current_area):
        index_flag = 0
        min_distance = start_node.get_distance(current_area[0])
        for index, node in enumerate(current_area[1:], 1):
            cur_distance = start_node.get_distance(node)
            if cur_distance < min_distance:
                min_distance = cur_distance
                index_flag = index
        self.total_distance += min_distance
        return current_area[index_flag]

    def find_route_in_area(self, start_node):
        current_area = self.area_list[start_node.area]
        current_area.remove(start_node)
        route = [start_node]
        while current_area:
            nearest_node = self.find_nearest_node(start_node, current_area)
            route.append(nearest_node)
            current_area.remove(nearest_node)
            start_node = nearest_node
        return route

    def find_neighbor_area(self, current_area, search_range):
        list_of_nodes = []
        for area in self.area_list.keys():
            if abs(area[0] - current_area[0]) <= search_range and \
                    abs(area[1] - current_area[1]) <= search_range:
                list_of_nodes += self.area_list[area]
        return list_of_nodes

    def find_nearest_out_area(self, start_node):
        current_area = start_node.area
        list_of_nodes = []
        search_range = 0
        while not list_of_nodes:
            search_range += 1
            list_of_nodes = self.find_neighbor_area(current_area, search_range)
        return self.find_nearest_node(start_node, list_of_nodes)

    def find_shortest_path(self):
        start_node = self.node_list[0]
        while self.area_list:
            self.route += self.find_route_in_area(start_node)
            del self.area_list[start_node.area]
            if len(self.route) < len(self.node_list):
                start_node = self.find_nearest_out_area(self.route[-1])
        return self.route
