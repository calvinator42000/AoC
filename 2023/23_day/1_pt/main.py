import sys

def solve(data):
    grid = parseData(data.split('\n'))
    start = (0,1)
    goal = (len(grid)-1,len(grid[0])-2)
    max_path = dfs(start, goal, grid)
    return len(max_path)

def dfs(start, end, grid):
    max_path = []
    stack = [(start, [])]
    while len(stack) > 0:
        current, curr_path = stack.pop()
        if current == end:
            if len(curr_path) > len(max_path):
                max_path = curr_path[:]
        for neighbor in getNeighbors(current, grid):
            if neighbor not in curr_path:
                stack.append((neighbor, curr_path + [neighbor]))
    return max_path

def getNeighbors(node, grid):
    dir_list = [(-1,0),(0,1),(1,0),(0,-1)]
    dir_syms = ['^','>','v','<']
    neighbors = []
    if grid[node[0]][node[1]] in dir_syms:
        dir = dir_list[dir_syms.index(grid[node[0]][node[1]])]
        next_node = (node[0]+dir[0], node[1]+dir[1])
        if 0 <= next_node[0] < len(grid) and 0 <= next_node[1] < len(grid[0]) and grid[next_node[0]][next_node[1]] != '#':
            neighbors.append(next_node)
    else:
        for dir in dir_list:
            next_node = (node[0]+dir[0], node[1]+dir[1])
            if 0 <= next_node[0] < len(grid) and 0 <= next_node[1] < len(grid[0]) and grid[next_node[0]][next_node[1]] != '#':
                neighbors.append(next_node)
    return neighbors

def printGrid(start, path, grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i,j) == start:
                print('S', end='')
            elif (i,j) in path:
                print('O', end='')
            else:
                print(grid[i][j], end='')
        print()

def parseData(line_list):
    grid = []
    for line in line_list:
        grid.append(list(line))
    return grid

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
