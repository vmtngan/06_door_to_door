#!/usr/bin/env python3
from sys import stderr
from time import time
from argparse import ArgumentParser
from node import Node
from algorithms import NearestNeighbor, BruteForce


def get_arguments():
    """
    Get and parse arguments from terminal.
    @return: list of arguments.
    """
    parser = ArgumentParser(description='Finding shortest path.',
                            usage='./tsp.py [filename] [algorithm]')
    parser.add_argument('filename', help='A file contains a list of cities')
    parser.add_argument('-a', '--algo', default='1',
                        help='Specify which algorithm to find')
    return parser.parse_args()


def read_data_file(filename):
    """
    Read information from data file and save each line to a list.
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
    @return: list of nodes
    """
    node_list = []
    for index, line in enumerate(data):
        city_info = line[:-1].split(', ')
        if len(city_info) == 3:
            try:
                node_list.append(Node(*city_info, index))
            except (TypeError, ValueError):
                stderr.write('Invalid file\n')
                exit(1)
        else:
            stderr.write('Invalid file\n')
            exit(1)
    return node_list


def main():
    # Dictionary contains algorithm classes
    algorithms = {'1': NearestNeighbor,
                  '2': BruteForce}
    arguments = get_arguments()
    data = read_data_file(arguments.filename)
    if data:
        # Set up a empty TSP map.
        tsp_map = None
        node_list = create_node_list(data)
        if arguments.algo in algorithms:
            tsp_map = algorithms[arguments.algo](node_list)
            tsp_map.find_shortest_path()
        print('Route:', tsp_map, sep='\n')
        print('Total of distance:', tsp_map.total_distance)
    else:
        stderr.write('Invalid file\n')
        exit(1)


if __name__ == '__main__':
    start = time()
    main()
    print('Runtime: {}s'.format(round(time() - start, 3)))
