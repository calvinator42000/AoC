import sys
import numpy as np
import networkx as nx

def parse_data(data):
    grid = np.array([list(line) for line in data.split('\n')])
    start = tuple(map(int, *zip(*np.where(grid == 'S'))))
    end = tuple(map(int, *zip(*np.where(grid == 'E'))))
    return grid, start, end

def create_graph(grid, start, end):
    graph = nx.DiGraph()
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    vertices = []
    for pos in zip(*np.where(grid != '#')):
        for i in range(4):
            vertices.append((tuple(map(int,pos)), i))
    graph.add_nodes_from(range(len(vertices)))
    start_id = vertices.index((start, 0))
    end_ids = [vertices.index((end, i)) for i in range(4)]
    for vertex_id in range(len(vertices)):
        vertex = vertices[vertex_id]
        v_pos, v_dir_index = vertex
        v_dir = directions[v_dir_index]
        left_id = vertices.index((v_pos, (v_dir_index-1)%4))
        right_id = vertices.index((v_pos, (v_dir_index+1)%4))
        graph.add_edge(vertex_id, left_id, weight=1000)
        graph.add_edge(vertex_id, right_id, weight=1000)
        forward_vertex = ((v_pos[0]+v_dir[0], v_pos[1]+v_dir[1]), v_dir_index)
        if grid[forward_vertex[0]] != '#':
            forward_id = vertices.index(forward_vertex, v_dir_index)
            graph.add_edge(vertex_id, forward_id, weight=1)
    return graph, vertices

def solve(data):
    grid, start, end = parse_data(data)
    graph, vertices = create_graph(grid, start, end)
    start_id = vertices.index((start, 0))
    end_ids = [vertices.index((end, i)) for i in range(4)]
    min_score = float('inf')
    best_path_generators = []
    for end_id in end_ids:
        score = nx.shortest_path_length(graph, start_id, end_id, weight="weight")
        if score < min_score:
            min_score = score
            best_path_generators.clear()
            best_paths = nx.all_shortest_paths(graph, start_id, end_id, weight="weight")
            best_path_generators.append(best_paths)
    best_tiles = set()
    for path_generator in best_path_generators:
        for path in path_generator:
            for tile in path:
                best_tiles.add(vertices[tile][0])
    return len(best_tiles)

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
