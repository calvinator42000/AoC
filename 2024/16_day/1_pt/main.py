import sys
import numpy as np

def parse_data(data):
    grid = np.array([list(line) for line in data.split('\n')])
    start = tuple(map(int, *zip(*np.where(grid == 'S'))))
    end = tuple(map(int, *zip(*np.where(grid == 'E'))))
    return grid, start, end

directions = [(0,1), (1,0), (0,-1), (-1,0)]

# Using Dijkstra's Algorithm
def dikjstras(grid, start):
    # Vertex is ((pos_x, pos_y), dir_index)
    vertices = []
    for pos in zip(*np.where(grid != '#')):
        for i in range(4):
            vertices.append((tuple(map(int,pos)), i))
    distances = dict.fromkeys(vertices, float('inf'))
    distances[(start, 0)] = 0
    processed = dict.fromkeys(vertices, False)
    queue = [(start, 0)]
    while queue:
        next_vertex = queue.pop(queue.index(min(queue, key = lambda x: distances[x])))
        v_pos, v_dir_index = next_vertex
        v_dir = directions[v_dir_index]
        v_dist = distances[next_vertex]
        processed[next_vertex] = True
        turn_left = ((v_pos, (v_dir_index-1)%4), v_dist+1000)
        turn_right = ((v_pos, (v_dir_index+1)%4), v_dist+1000)
        move_forward = (((v_pos[0]+v_dir[0], v_pos[1]+v_dir[1]), v_dir_index), v_dist+1)
        for opt in turn_left, turn_right, move_forward:
            if grid[opt[0][0]] != '#':
                if not processed[opt[0]]:
                    distances[opt[0]] = min(distances[opt[0]], opt[1])
                    queue.append(opt[0])
    return distances

def solve(data):
    grid, start, end = parse_data(data)
    distances = dikjstras(grid, start)
    min_score = float('inf')
    for i in range(4):
        min_score = min(distances[(end, i)], min_score)
    return min_score

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
