import sys

def main(data):
    grid = parseData(data.split('\n'))
    cycles = 1000000000
    res_cache = {}
    load_index = []
    cycle = 0
    while cycle < cycles+1:
        tuple_grid = tuple(map(tuple, grid))
        if tuple_grid in res_cache.keys():
            cycle_beg = res_cache[tuple_grid]
            return load_index[cycle_beg + ((cycles-cycle_beg) % (cycle-cycle_beg))]
        else:
            tuple_grid = tuple(map(tuple, grid))
            res_cache[tuple_grid] = cycle
            load_index.append(getLoad(grid))
            grid = runCycle(grid)
            cycle += 1
    return getLoad(grid)

def getLoad(grid):
    load = 0
    for row_i in range(len(grid)):
        for col in grid[row_i]:
            if col == 'O':
                load += len(grid) - row_i
    return load

def runCycle(grid):
    grid = rotateGrid90(grid)
    for x in range(4):
        for row in grid:
            rock_num = 0
            for col_i in range(len(grid[0])):
                if row[col_i] == '#':
                    for r in range(col_i-rock_num, col_i):
                        row[r] = 'O'
                    rock_num = 0
                elif row[col_i] == 'O':
                    row[col_i] = '.'
                    rock_num += 1
            for r in range(len(row)-rock_num, len(row)):
                row[r] = 'O'
        grid = rotateGrid90(grid)
    grid = rotateGrid270(grid)
    return grid

def rotateGrid90(grid):
    rev_grid = list(reversed(grid))
    inv_grid = list(map(list, zip(*rev_grid)))
    return inv_grid

def rotateGrid270(grid):
    return list(map(list, zip(*grid)))[::-1]

def printGrid(grid):
    for row in grid:
        for col in row:
            print(col, end="")
        print()
    return

def parseData(line_list):
    grid = []
    for row in line_list:
        grid.append(list(row))
    return grid

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))