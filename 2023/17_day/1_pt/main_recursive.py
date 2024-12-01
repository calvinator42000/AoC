import sys

def solve(data):
    grid = parseData(data.split('\n'))
    node_dict = {}
    loc_list = [(i,j) for i in range(len(grid)) for j in range(len(grid[0]))]
    dir_list = [(0,1),(0,-1),(1,0),(-1,0)]
    for loc in loc_list:
        for dir in dir_list:
            for straight_count in range(3):
                node_dict[(loc,dir,straight_count)] = sys.maxsize
    min_heat_loss = sys.maxsize
    node_dict[((0,0),(0,1),-1)] = 0
    node_dict[((0,0),(1,0),-1)] = 0    
    min_heat_loss = traverse((0,0), (1,0), -1, [], grid, sys.maxsize, node_dict)
    min_heat_loss = traverse((0,0), (0,1), -1, [], grid, min_heat_loss, node_dict)
    return min_heat_loss

def traverse(curr_loc, curr_dir, curr_straight_count, path, grid, min_heat_loss, node_dict):
    next_dir_list = [(curr_dir[1]*-1, curr_dir[0]*-1), curr_dir, (curr_dir[1], curr_dir[0])]
    step_config_list = []
    for next_dir in next_dir_list:
        if next_dir == curr_dir:
            next_straight_count = curr_straight_count + 1
        else:
            next_straight_count = 0
        ## If straight line limit has been exceeded
        if next_straight_count > 2:
            continue
        next_loc = (curr_loc[0] + next_dir[0], curr_loc[1] + next_dir[1])
        ## If location is outside of the grid, skip
        if next_loc[0] < 0 or next_loc[0] >= len(grid) or next_loc[1] < 0 or next_loc[1] >= len(grid[0]):
            continue
        ## If location has already been visited, skip
        if next_loc in path:
            continue
        next_path = path+[next_loc]
        next_heat_loss = node_dict[(curr_loc,curr_dir,curr_straight_count)] + grid[next_loc[0]][next_loc[1]]
        ## If the current heat loss exceeds the record lowest heat loss or if a path to this node has a lesser heat loss
        if next_heat_loss >= min_heat_loss or next_heat_loss >= node_dict[(next_loc,next_dir, next_straight_count)]:
            continue
        node_dict[(next_loc,next_dir,next_straight_count)] = next_heat_loss
        ## If the target location has been reached
        if next_loc == (len(grid)-1, len(grid[0])-1):
            min_heat_loss = min(next_heat_loss, min_heat_loss)
            continue
        step_config_list.append((next_loc, next_dir, next_straight_count, next_path, grid))
    step_config_list.sort(key = lambda x: node_dict[(x[0],x[1],x[2])])
    for step_config in step_config_list:
        min_heat_loss = traverse(*step_config, min_heat_loss, node_dict)
    return min_heat_loss

def processPath(path, grid):
    new_grid = list(map(list,grid))
    sum = 0
    for node in path:
        sum += new_grid[node[0]][node[1]]
        new_grid[node[0]][node[1]] = '#'
    print(f"Sum: {sum}")
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
    print(solve(open(sys.argv[1]).read().rstrip()))
