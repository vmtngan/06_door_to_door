from itertools import permutations
from graph import Graph


def get_total_distance(route_list):
    """
    Calculate the total distance of a route.
    @param route_list: list of nodes corresponding to a route
    @return: the total distance of a route
    """
    total_distance = 0
    for index, node in enumerate(route_list[:-1]):
        total_distance += node.get_distance(route_list[index + 1])
    return total_distance


class BruteForce(Graph):
    """
    Find the shortest path through all cities by brute-force.
    Not available for large maps (over 10 cities).
    """
    def find_shortest_path(self):
        """
        Find the shortest path by brute-force.
        @return: a shortest route (relative accuracy)
        """
        # Check the graph containing less than 10 nodes
        if len(self.node_list) > 10:
            print('Too much cities')
            exit()
        # Set up the starting node
        start = self.node_list[0]
        # Get the list of permutations of the node list
        route_list = [perm for perm in permutations(self.node_list)
                      if perm[0] == start]
        # Calculate the total distance with each permutation route.
        distance_list = [get_total_distance(item) for item in route_list]
        # Take the shortest distance in distance_list
        min_distance = min(distance_list)
        # Add the min_distance to self.total_distance
        self.total_distance += min_distance
        # Assign the shortest route to self.route
        self.route = route_list[distance_list.index(min_distance)]
        return self.route


class NearestNeighbor(Graph):
    """ Use Nearest Neighbor algorithm (optimized version) to solve TSP."""
    def find_nearest_node(self, start_node, current_area):
        """
        Find the closest node to start_node.
        @param start_node: the starting node
        @param current_area: the current area
        @return: a closest node in current area
        """
        index_flag = 0
        min_distance = start_node.get_distance(current_area[0])
        for index, node in enumerate(current_area[1:], 1):
            # Calculate distance between two nodes
            cur_distance = start_node.get_distance(node)
            if cur_distance < min_distance:
                min_distance = cur_distance
                index_flag = index
        # Add the min_distance to self.total_distance
        self.total_distance += min_distance
        return current_area[index_flag]

    def find_route_in_area(self, start_node):
        """
        Find the shortest route in the current area.
        @param start_node: the starting node
        @return: the shortest route in the current area
        """
        # Get list of nodes in current area
        current_area = self.area_list[start_node.area]
        # Remove the starting node from list of nodes in current area
        current_area.remove(start_node)
        # Set up first element of route
        route = [start_node]
        while current_area:
            # Find the closest node to start_node in current_area
            nearest_node = self.find_nearest_node(start_node, current_area)
            route.append(nearest_node)
            current_area.remove(nearest_node)
            # Reset up the starting node
            start_node = nearest_node
        return route

    def find_neighbor_area(self, current_area, search_range):
        """
        Find node list of neighbor area with search range.
        @param current_area: the current area
        @param search_range: the search range
        @return: node list of neighbor area
        """
        list_of_nodes = []
        for area in self.area_list.keys():
            if (abs(area[0] - current_area[0]) <= search_range and
                    abs(area[1] - current_area[1]) <= search_range):
                list_of_nodes += self.area_list[area]
        return list_of_nodes

    def find_nearest_out_area(self, start_node):
        """
        Find the nearest node of out area
        @param start_node: the starting node
        @return: a nearest node of out area
        """
        current_area = start_node.area
        list_of_nodes = []
        search_range = 0
        while not list_of_nodes:
            search_range += 1
            list_of_nodes = self.find_neighbor_area(current_area, search_range)
        return self.find_nearest_node(start_node, list_of_nodes)

    def find_shortest_path(self):
        """
        Find the shortest path by Nearest Neighbor algorithm.
        @return: a shortest route (relative accuracy)
        """
        # Set up the starting node
        start_node = self.node_list[0]
        while self.area_list:
            # Add route in current area to self.route
            self.route += self.find_route_in_area(start_node)
            # Delete current area from self.area_list
            del self.area_list[start_node.area]
            # Check the number of nodes in self.route
            # is less than self.node_list
            if len(self.route) < len(self.node_list):
                # Reset up the starting node
                start_node = self.find_nearest_out_area(self.route[-1])
        return self.route
