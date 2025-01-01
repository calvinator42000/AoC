import sys
import numpy as np
import networkx as nx

def parse_data(data):
    grid = np.array([list(line) for line in data.split('\n')])
    start = tuple(map(int, *zip(*np.where(grid == 'S'))))
    end = tuple(map(int, *zip(*np.where(grid == 'E'))))
    return grid, start, end

directions = [(0,1), (1,0), (0,-1), (-1,0)]

def create_graph(grid):
    graph = nx.Graph()
    graph.add_nodes_from([tuple(map(int, node)) for node in zip(*np.where(grid != '#'))])
    for node in graph.nodes:
        for dir in directions:
            next_node = (node[0]+dir[0], node[1]+dir[1])
            if next_node in graph.nodes:
                graph.add_edge(node, next_node)
    return graph

def get_euclidean_distance(source, target):
    return abs(source[0]-target[0]) + abs(source[1]-target[1])

def solve(data):
    cheat_duration = 20
    grid, start, end = parse_data(data)
    graph = create_graph(grid)
    path = nx.shortest_path(graph, start, end)[::-1]
    distances_from_end = dict(nx.single_target_shortest_path_length(graph, end))
    target_cheats = 0
    # Testing what happens when we activate the cheat on "node"
    for node in graph.nodes:
        curr_dist = distances_from_end[node]
        # Get closest node to the end that fits within a euclidean distance allowed by the cheat duration
        for target in path:
            cheat_dist = distances_from_end[target]
            euclidean_distance = get_euclidean_distance(node, target)
            # Does the cheat save at least 100 picoseconds?
            if curr_dist - cheat_dist - euclidean_distance >= 100:
                # Can you get there with a cheat?
                if euclidean_distance <= cheat_duration:
                    target_cheats += 1
    return target_cheats

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
