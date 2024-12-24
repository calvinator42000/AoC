import sys
import numpy as np
import math

def parse_data(data):
    line_list = data.split('\n')
    grid = []
    line_i = 0
    while line_list[line_i]:
        grid.append(list(line_list[line_i]))
        line_i += 1
    grid = np.array(grid)
    path = ""
    while line_i < len(line_list):
        path += line_list[line_i]
        line_i += 1
    return grid, path

def move(robot, dir, grid):
    next_pos = (robot[0]+dir[0], robot[1]+dir[1])
    num_boxes = 0
    edge_of_move = next_pos
    while grid[edge_of_move] == 'O':
        edge_of_move = (edge_of_move[0]+dir[0], edge_of_move[1]+dir[1])
        num_boxes += 1
    if grid[edge_of_move] != '#':
        while edge_of_move != robot:
            pull_pos = (edge_of_move[0]-dir[0], edge_of_move[1]-dir[1])
            grid[edge_of_move] = grid[pull_pos]
            edge_of_move = pull_pos
        grid[edge_of_move] = '.'
        return next_pos
    return robot

def solve(data):
    directions = {'>':(0,1), 'v':(1,0), '<':(0,-1), '^':(-1,0)}
    grid, path = parse_data(data)
    # Assumes just one robot
    robot_pos = tuple(map(int,*zip(*np.where(grid == '@'))))
    for dir in path:
        robot_pos = move(robot_pos, directions[dir], grid)
    box_locations = list(zip(*np.where(grid == 'O')))
    total_gps = 0
    for box in box_locations:
        total_gps += 100*box[0] + box[1]
    return total_gps

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
