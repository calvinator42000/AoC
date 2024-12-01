import sys

def solve(data):
    grid = parseData(data.split('\n'))
    # min_heat_loss = traverse(grid, 1, 3)
    min_heat_loss = traverse(grid, 4, 10)
    return min_heat_loss

def traverse(grid, min_straight, max_straight):
    min_heat_loss = sys.maxsize
    node_dict = {}
    queue = []
    ## Queue Entry Format: (loc, dir, straight)
    queue.append(((0,0), (0,1), 1))
    node_dict[((0,0), (0,1), 1)] = 0
    queue.append(((0,0), (1,0), 1))
    node_dict[((0,0), (1,0), 1)] = 0
    while len(queue) > 0:
        node = queue.pop(0)
        loc, dir, straight = node
        next_dir_list = [(dir[1]*-1, dir[0]*-1), dir, (dir[1], dir[0])]
        for next_dir in next_dir_list:
            if next_dir == dir:
                next_straight = straight + 1
            else:
                if straight < min_straight:
                    continue
                next_straight = 1
            if next_straight <= max_straight:
                next_loc = (loc[0] + next_dir[0], loc[1] + next_dir[1])
                if 0 <= next_loc[0] < len(grid) and 0 <= next_loc[1] < len(grid[0]):
                    next_node = (next_loc, next_dir, next_straight)
                    next_heat = node_dict[node] + grid[next_loc[0]][next_loc[1]]
                    if not next_node in node_dict.keys():
                        node_dict[next_node] = sys.maxsize
                    if next_heat < min_heat_loss and next_heat < node_dict[next_node]:
                        node_dict[next_node] = next_heat
                        if next_loc == (len(grid)-1, len(grid[0])-1) and next_straight > 3:
                            min_heat_loss = min(next_heat, min_heat_loss)
                        else:
                            queue.append(next_node)
    return min_heat_loss

def parseData(line_list):
    grid = []
    for line in line_list:
        grid.append(tuple(map(int, line)))
    return tuple(grid)

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
