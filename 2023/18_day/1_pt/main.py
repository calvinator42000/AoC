import sys

def solve(data):
    inst_list = parseData(data.split('\n'))
    grid, path_len = graph_edge(inst_list)
    lagoon_size = path_len + fill_interior(grid)
    return lagoon_size

def fill_interior(grid):
    dot = find_dot(grid)
    dir_list = [(-1,0),(0,1),(1,0),(0,-1)]
    while dot:
        valid_area = True
        area_size = 1
        queue = [dot]
        while len(queue) > 0:
            dot = queue.pop(0)
            grid[dot[0]][dot[1]] = '#'
            for dir in dir_list:
                next_dot = (dot[0]+dir[0], dot[1]+dir[1])
                if 0 <= next_dot[0] < len(grid) and 0 <= next_dot[1] < len(grid[0]):
                    if grid[next_dot[0]][next_dot[1]] == '.':
                        if not next_dot in queue:
                            queue.append(next_dot)
                            area_size += 1
                else:
                    valid_area = False
        if valid_area:
            return area_size
        dot = find_dot(grid)
    return None

def find_dot(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                return (i,j)
    return None

def graph_edge(inst_list):
    start, graph_dims = get_graph_dims(inst_list)
    grid = []
    for row in range(graph_dims[0]):
        grid.append(['.']*graph_dims[1])
    dir_dict = {'U':(-1,0),'R':(0,1),'D':(1,0),'L':(0,-1)}
    loc = start
    path_len = 0
    for inst in inst_list:
        dir, steps, color = inst
        dir_offset = dir_dict[dir]
        for step in range(steps):
            loc = (loc[0]+dir_offset[0], loc[1]+dir_offset[1])
            grid[loc[0]][loc[1]] = '#'
            path_len += 1
    return (grid, path_len)

def get_graph_dims(inst_list):
    min_row = 0
    max_row = 0
    min_col = 0
    max_col = 0
    curr_row = 0
    curr_col = 0
    for inst in inst_list:
        dir, steps, color = inst
        if dir == 'U':
            curr_col -= steps
            min_col = min(min_col, curr_col)
        elif dir == 'R':
            curr_row += steps
            max_row = max(max_row, curr_row)
        elif dir == 'D':
            curr_col += steps
            max_col = max(max_col, curr_col)
        elif dir == 'L':
            curr_row -= steps
            min_row = min(min_row, curr_row)
    row_size = max_row - min_row + 1
    col_size = max_col - min_col + 1
    start = (abs(min_col), abs(min_row))
    return (start, (col_size, row_size))

def printGrid(grid):
    for row in grid:
        print("".join(row))
    print()
    return

def parseData(line_list):
    inst_list = []
    for line in line_list:
        dir, steps, color = line.split(' ')
        inst_list.append((dir, int(steps), color))
    return inst_list

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
