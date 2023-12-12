import sys

def main(data):
    grid = getExpandedGalaxy(data.split('\n'))
    gal_list = getGalaxies(grid)
    path_sum = 0
    for i in range(len(gal_list)):
        for j in range(i+1,len(gal_list)):
            path_sum += abs(gal_list[i][0]-gal_list[j][0]) + abs(gal_list[i][1]-gal_list[j][1])
    return path_sum

def getGalaxies(grid):
    gal_list = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '#':
                gal_list.append((row,col))
    return gal_list

def getExpandedGalaxy(line_list):
    grid = []
    cols_wo_gals = list(range(len(line_list[0])))
    for line in line_list:
        if line == "."*len(line):
            grid.append(line)
            grid.append(line)
        else:
            for col in range(len(line)):
                if line[col] == '#':
                    try:
                        cols_wo_gals.remove(col)
                    except ValueError:
                        pass
            grid.append(line)
    cols_wo_gals.sort(reverse=True)
    for row in range(len(grid)):
        for col in cols_wo_gals:
            grid[row] = grid[row][:col] + '.' + grid[row][col:]
    return grid


if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))
