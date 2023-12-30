import sys

## Solution Derived from this beautiful explanation: https://github.com/villuna/aoc23/wiki/A-Geometric-solution-to-advent-of-code-2023,-day-21

class Node:
    def __init__(self, loc, grid):
        self.loc = loc
        self.neighbors = []
        dir_list = [(-1,0),(0,1),(1,0),(0,-1)]
        for dir in dir_list:
            next_loc = (loc[0]+dir[0], loc[1]+dir[1])
            if 0 <= next_loc[0] < len(grid) and 0 <= next_loc[1] < len(grid[0]) and grid[next_loc[0]][next_loc[1]] == '.':
                self.neighbors.append(next_loc)

def main(data):
    start, grid = parseData(data.split('\n'))
    step_count = 64
    visited = {start: 0}
    possible_nodes = [start]
    for step in range(step_count):
        next_possible_nodes = []
        while len(possible_nodes) > 0:
            node = Node(possible_nodes.pop(0), grid)
            for neighbor in node.neighbors:
                if not neighbor in next_possible_nodes:
                    if not neighbor in visited:
                        next_possible_nodes.append(neighbor)
                        visited[neighbor] = step
        possible_nodes = []+next_possible_nodes
    solution = 0
    for d in visited.values():
        if d % 2 == step_count % 2:
            solution += 1
    return solution


def parseData(line_list):
    start = None
    grid = []
    for i in range(len(line_list)):
        line = list(line_list[i])
        if 'S' in line:
            start = (i, line.index('S'))
            line[line.index('S')] = '.'
        grid.append(line)
    return (start, grid)

def printGrid(grid):
    for line in grid:
        print("".join(line))
    print()
    return None

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))
