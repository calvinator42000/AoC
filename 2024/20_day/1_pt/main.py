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

def get_cheats(node, grid, graph):
    cheat_positions = []
    for dir in directions:
        step_1 = (node[0]+dir[0], node[1]+dir[1])
        step_2 = (node[0]+dir[0]*2, node[1]+dir[1]*2)
        if step_2 in graph.nodes and grid[step_1] == '#':
            cheat_positions.append(step_2)
    return cheat_positions

def solve(data):
    grid, start, end = parse_data(data)
    graph = create_graph(grid)
    distances_from_end = dict(nx.single_target_shortest_path_length(graph, end))
    target_cheats = 0
    for node in graph.nodes:
        cheat_positions = get_cheats(node, grid, graph)
        curr_dist = distances_from_end[node]
        for cheat in cheat_positions:
            cheat_dist = distances_from_end[cheat]
            if curr_dist - cheat_dist - 2 >= 100:
                target_cheats += 1
    return target_cheats

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
