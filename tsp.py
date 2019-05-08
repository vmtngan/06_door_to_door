#!/usr/bin/env python3
from sys import stderr
from time import time
from argparse import ArgumentParser
from node import Node
from algorithms import NearestNeighbor, BruteForce


def get_arguments():
    """
    Get and parse arguments from terminal.
    @return: namespace of arguments
    """
    parser = ArgumentParser(description='Finding shortest path.',
                            usage='./tsp.py [filename] [algorithm]')
    parser.add_argument('filename', help='A file contains a list of cities')
    parser.add_argument('-a', '--algo', default='1',
                        help='Specify which algorithm to find')
    return parser.parse_args()


def read_data_file(filename):
    """
    Read information from data file.
    Save each line to a list.
    @param filename: file contains data of cities information
    @return: list of each line in the data file
    """
    try:
        with open(filename, 'r') as data_file:
            return data_file.readlines()
    except (FileNotFoundError, PermissionError,
            IsADirectoryError, UnicodeDecodeError):
        stderr.write('Invalid file\n')
        exit(1)


def create_node_list(data):
    """
    Create a list of nodes taken from each line list.
    @param data: list of each line in the data file
    @return: list of Node objects
    """
    node_list = []
    for line in data:
        # A line contains city information with 3 parameters in order:
        # city name, longitude, latitude
        city_info = line[:-1].split(', ')
        # Check one line contains all 3 parameters
        if len(city_info) == 3:
            try:
                node_list.append(Node(*city_info))
            except (TypeError, ValueError):
                stderr.write('Invalid file\n')
                exit(1)
        else:
            stderr.write('Invalid file\n')
            exit(1)
    return node_list


def main():
    """
    Run the main program.
    """
    # Dictionary contains algorithm classes
    algorithms = {'1': NearestNeighbor, '2': BruteForce}
    arguments = get_arguments()
    # List of each line in the data file
    data = read_data_file(arguments.filename)
    # Check data is empty
    if data:
        # Set up a empty TSP map
        tsp_map = None
        # List of Node objects
        node_list = create_node_list(data)
        # Initialize Graph and run corresponding algorithm
        if arguments.algo in algorithms:
            tsp_map = algorithms[arguments.algo](node_list)
            tsp_map.find_shortest_path()
        # Display results to screen
        print('Route:', tsp_map, sep='\n')
        print('Total of distance:', tsp_map.total_distance)
    else:
        stderr.write('Invalid file\n')
        exit(1)


if __name__ == '__main__':
    start = time()
    main()
    print('Runtime: {}s'.format(round(time() - start, 3)))
