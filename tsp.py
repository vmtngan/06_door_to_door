#!/usr/bin/env python3
from sys import stderr
from time import time
from argparse import ArgumentParser
from node import Node
from algorithms import NearestNeighbor


def get_arguments():
    parser = ArgumentParser(description='Finding shortest path.',
                            usage='./tsp.py [filename] [algorithm]')
    parser.add_argument('filename', help='A file contains a list of cities')
    parser.add_argument('--algo', default='1',
                        help='Specify which algorithm to find')
    return parser.parse_args()


def read_data_file(filename):
    try:
        with open(filename, 'r') as data_file:
            return data_file.readlines()
    except (FileNotFoundError, PermissionError, IsADirectoryError):
        stderr.write('Invalid file\n')
        exit(1)


def create_node_list(data):
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
    arguments = get_arguments()
    data = read_data_file(arguments.filename)
    node_list = create_node_list(data)
    tsp_map = NearestNeighbor(node_list)
    # for key, value in sorted(tsp_map.area_list.items()):
    #     print('{}: {}'.format(key,
    #                           ', '.join([node.city_name for node in value])))
    tsp_map.find_shortest_path()
    print(tsp_map)
    print(tsp_map.total_distance)


if __name__ == '__main__':
    start = time()
    main()
    print('Main: {}s'.format(time() - start))
