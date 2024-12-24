import sys
import numpy as np

def parse_data(data):
    line_list = data.split('\n')
    grid = []
    line_i = 0
    while line_list[line_i]:
        grid.append(list(line_list[line_i].replace('#','##').replace('O','[]').replace('.','..').replace('@','@.')))
        line_i += 1
    grid = np.array(grid)
    path = ""
    while line_i < len(line_list):
        path += line_list[line_i]
        line_i += 1
    return grid, path

def move(robot, dir, grid):
    if dir[0]:
        return move_vert(robot, dir, grid)
    else:
        return move_horz(robot, dir, grid)

def move_vert(robot, dir, grid):
    next_pos = (robot[0]+dir[0], robot[1]+dir[1])
    pushed_boxes = [{robot}]
    checking_boxes = True
    wall_found = False
    while checking_boxes and not wall_found:
        checking_boxes = False
        new_layer = set()
        for box in pushed_boxes[-1]:
            check_pos = (box[0]+dir[0], box[1]+dir[1])
            if grid[check_pos] == '[':
                checking_boxes = True
                new_layer.add(check_pos)
                new_layer.add((check_pos[0], check_pos[1]+1))
            elif grid[check_pos] == ']':
                checking_boxes = True
                new_layer.add(check_pos)
                new_layer.add((check_pos[0], check_pos[1]-1))
            elif grid[check_pos] == '#':
                wall_found = True
                break
        if checking_boxes:
            pushed_boxes.append(new_layer)
    if not wall_found:
        for layer in pushed_boxes[::-1]:
            for pos in layer:
                push_pos = (pos[0]+dir[0], pos[1]+dir[1])
                grid[push_pos] = grid[pos]
                grid[pos] = '.'
        return next_pos
    return robot

def move_horz(robot, dir, grid):
    next_pos = (robot[0]+dir[0], robot[1]+dir[1])
    num_boxes = 0
    edge_of_move = next_pos
    while grid[edge_of_move] in '[]':
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
    box_locations = list(zip(*np.where(grid == '[')))
    total_gps = 0
    for box in box_locations:
        total_gps += 100*box[0] + box[1]
    return total_gps

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
