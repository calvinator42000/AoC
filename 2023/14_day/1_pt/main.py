import sys

def main(data):
    grid = parseData(data.split('\n'))
    load = getLoad(grid)
    return load

def getLoad(grid):
    grid = rotateGrid90(grid)
    load = 0
    for row in grid:
        rock_num = 0
        for i in range(len(row)):
            if row[i] == '#':
                load += sum(range(i+1-rock_num, i+1))
                rock_num = 0
            elif row[i] == 'O':
                rock_num += 1
        load += sum(range(len(row)+1-rock_num, len(row)+1))
    return load

def rotateGrid90(grid):
    rev_grid = list(reversed(grid))
    inv_grid = list(zip(*rev_grid))
    return inv_grid

def parseData(line_list):
    grid = []
    for row in line_list:
        grid.append(list(row))
    return grid

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))