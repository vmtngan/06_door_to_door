from abc import ABC, abstractmethod


class Graph(ABC):
    """Represents a graph containing many nodes (cities)."""
    def __init__(self, node_list):
        """
        Initialize attributes of the Graph class.
        @param node_list: list of Node objects
        """
        self.node_list = node_list
        self.route = []
        self.total_distance = 0
        self.latitude_list = [node.latitude for node in self.node_list]
        self.longitude_list = [node.longitude for node in self.node_list]
        self.min_x = min(self.latitude_list) - 1
        self.max_x = max(self.latitude_list) + 1
        self.min_y = min(self.longitude_list) - 1
        self.max_y = max(self.longitude_list) + 1
        self.div_num = 1.5 * len(node_list) ** 0.5
        self.unit = (self.max_x - self.min_x) / self.div_num
        self.area_list = self.split_graph()

    def split_graph(self):
        """
        Divide the graph into many small areas.
        @return: a dictionary with:
                    - key: area address
                    - value: list of nodes (cities) in that area.
        """
        area_list = {}
        for node in self.node_list:
            # Get the area address of node
            node.area = (int(node.latitude // self.unit),
                         int(node.longitude // self.unit))
            # Save node to dictionary
            if node.area in area_list:
                area_list[node.area].append(node)
            else:
                area_list[node.area] = [node]
        return area_list

    def __str__(self):
        """
        Override the __str__
        @return: road map after finding the shortest path.
        """
        return ' -> '.join([node.city_name for node in self.route])

    @abstractmethod
    def find_shortest_path(self):
        """Find the solution to the problem."""
        return
