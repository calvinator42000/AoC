import sys

def solve(data):
    start, grid = parseData(data.split('\n'))
    ## Solution assumes that the start is in the middle of the input and that the input is a square of odd dimensions
    steps = steps = 26501365
    evens_odds = getEvensOdds(start, grid)
    grid_size = len(grid)
    geometric_sol = solveGeometric(grid_size, steps, evens_odds)
    quadratic_sol = solveQuadratic(grid_size, steps, evens_odds)
    assert geometric_sol == quadratic_sol
    return geometric_sol

def solveQuadratic(grid_size, steps, evens_odds):
    ## Solution derviced from this beautiful explanation: https://colab.research.google.com/github/derailed-dash/Advent-of-Code/blob/master/src/AoC_2023/Dazbo's_Advent_of_Code_2023.ipynb#scrollTo=Day_21_Part_2
    points = {65:0,196:0,327:0}
    for key in points.keys():
        points[key] = solveGeometric(grid_size, key, evens_odds)
    points = list(points.values())
    c = points[0]
    b = (4*points[1] - 3*points[0] - points[2]) // 2
    a = points[1] - points[0] - b
    x = (steps - grid_size//2) // grid_size
    return a*x**2 + b*x + c

def solveGeometric(grid_size, steps, evens_odds):
    ## Solution derived from this beautiful explanation: https://github.com/villuna/aoc23/wiki/A-Geometric-solution-to-advent-of-code-2023,-day-21
    even_nodes, odd_nodes, even_corner_nodes, odd_corner_nodes = evens_odds
    n = int((steps-int(grid_size/2)) / grid_size)
    ## I don't have a good explanation as to why I have to include "-n" into the expression, but it works!
    total = ((n+1)**2)*odd_nodes + (n**2)*even_nodes + (n)*even_corner_nodes - (n+1)*odd_corner_nodes - n
    return total

def getEvensOdds(start, grid):
    ## even_odd_count = [<evens>,<odds>]
    even_odd_count = [1, 0]
    corner_even_odd_count = [0, 0]
    visited = [start]
    possible_nodes = [start]
    step = 1
    while len(possible_nodes) > 0:
        next_possible_nodes = []
        while len(possible_nodes) > 0:
            neighbors = getNeighbors(possible_nodes.pop(0), grid)
            for neighbor in neighbors:
                if not neighbor in next_possible_nodes:
                    if not neighbor in visited:
                        next_possible_nodes.append(neighbor)
                        visited.append(neighbor)
                        even_odd_count[step % 2] += 1
                        if step > int((len(grid)-1)/2):
                            corner_even_odd_count[step % 2] += 1
        possible_nodes = []+next_possible_nodes
        step += 1
    return *even_odd_count, *corner_even_odd_count

def getNeighbors(loc, grid):
    neighbors = []
    dir_list = [(-1,0),(0,1),(1,0),(0,-1)]
    for dir in dir_list:
        next_loc = (loc[0]+dir[0], loc[1]+dir[1])
        if 0 <= next_loc[0] < len(grid) and 0 <= next_loc[1] < len(grid[0]) and grid[next_loc[0]][next_loc[1]] == '.':
            neighbors.append(next_loc)
    return neighbors

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

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
