import sys
import networkx as nx
import numpy as np

def create_graph(grid):
    graph = nx.Graph()
    graph.add_nodes_from([tuple(map(int, node)) for node in zip(*np.where(grid == '.'))])
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    for node in graph.nodes:
        for dir in directions:
            next_node = (node[0]+dir[0], node[1]+dir[1])
            if next_node in graph.nodes:
                graph.add_edge(node, next_node)
    return graph

def solve(data):
    grid_shape = (71,71)
    grid = np.full(grid_shape, '.')
    fallen_bytes = [tuple(map(int, line.split(','))) for line in data.split('\n')[:1024]]
    for byte in fallen_bytes:
        grid[byte] = '#'
    graph = create_graph(grid)
    steps = nx.shortest_path_length(graph, (0,0), (70,70))
    return steps

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
