import sys

class Node:
    def __init__(self, loc, min_heat_loss=sys.maxsize, visited=False):
        self.loc = loc
        self.min_heat_loss = min_heat_loss
        self.visited = visited

def main(data):
    grid = parseData(data.split('\n'))
    node_dict = {}
    loc_list = [(i,j) for i in range(len(grid)) for j in range(len(grid[0]))]
    for loc in loc_list:
        node_dict[loc] = Node(loc)
    node_dict[(0,-1)] = Node((0,-1),0,True)
    traverse2((0,-1), (0,1), 0, 0, grid, node_dict)
    print(node_dict[(len(grid)-1, len(grid[0])-1)].min_heat_loss)
    return 0

def traverse2(curr_loc, curr_dir, curr_heat_loss, curr_straight_count, grid, node_dict, path=[]):
    next_dir_list = [(curr_dir[1]*-1, curr_dir[0]*-1), curr_dir, (curr_dir[1], curr_dir[0])]
    step_config_list = []
    for next_dir in next_dir_list:
        next_loc = (curr_loc[0] + next_dir[0], curr_loc[1] + next_dir[1])
        if next_loc[0] < 0 or next_loc[0] >= len(grid) or next_loc[1] < 0 or next_loc[1] >= len(grid[0]):
            continue
        next_heat_loss = curr_heat_loss+grid[next_loc[0]][next_loc[1]]
        if next_dir == curr_dir:
            if curr_straight_count == 2:
                continue
            next_straight_count = curr_straight_count + 1
        else:
            next_straight_count = 0
        if node_dict[next_loc].visited:
            continue
        node_dict[next_loc].min_heat_loss = min(node_dict[next_loc].min_heat_loss, next_heat_loss)
        step_config_list.append((next_loc, next_dir, next_heat_loss, next_straight_count))
    step_config_list.sort(key = lambda x: x[2])
    node_dict[curr_loc].visited = True
    for step_config in step_config_list:
        if step_config[0] == (len(grid)-1, len(grid[0])-1):
            printGrid(processPath(path + [step_config[0]],grid))
        path = traverse2(*step_config, grid, node_dict, path + [step_config[0]])
    return path

def traverse(curr_loc, curr_dir, curr_heat_loss, curr_straight_count, path, grid, min_heat_loss):
    next_dir_list = [(curr_dir[1]*-1, curr_dir[0]*-1), curr_dir, (curr_dir[1], curr_dir[0])]
    step_config_list = []
    for next_dir in next_dir_list:
        next_loc = (curr_loc[0] + next_dir[0], curr_loc[1] + next_dir[1])
        if next_loc[0] < 0 or next_loc[0] >= len(grid) or next_loc[1] < 0 or next_loc[1] >= len(grid[0]):
            continue
        if next_loc in path:
            continue
        next_heat_loss = curr_heat_loss+grid[curr_loc[0]][curr_loc[1]]
        if next_heat_loss > min_heat_loss:
            continue
        if next_loc == (len(grid)-1, len(grid[0])-1):
            # printGrid(processPath(path, grid))
            print(min(next_heat_loss, min_heat_loss))
            min_heat_loss = min(next_heat_loss, min_heat_loss)
            continue
        if next_dir == curr_dir:
            next_straight_count = curr_straight_count + 1
        else:
            next_straight_count = 0
        if next_straight_count > 2:
            continue
        next_path = path+[next_loc]
        step_config_list.append((next_loc, next_dir, next_heat_loss, next_straight_count, next_path, grid))
    step_config_list.sort(key = lambda x: x[2])
    for step_config in step_config_list:
        min_heat_loss = traverse(*step_config, min_heat_loss)
    return min_heat_loss

def processPath(path, grid):
    new_grid = list(map(list,grid))
    for node in path:
        new_grid[node[0]][node[1]] = '#'
    return tuple(new_grid)

def printGrid(grid):
    for row in grid:
        for col in row:
            print(col, end="")
        print()
    print()
    return

def parseData(line_list):
    grid = []
    for line in line_list:
        grid.append(tuple(map(int, line)))
    return tuple(grid)

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))
