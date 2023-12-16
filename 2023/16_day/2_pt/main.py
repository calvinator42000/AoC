import sys

def main(data):
    grid = parseData(data.split('\n'))
    most_energized = 0
    for row_i in range(len(grid)):
        path = {}
        moveBeam((row_i,-1), (0,1), grid, path)
        most_energized = max(len(set(path.values()))-1, most_energized)
        path = {}
        moveBeam((row_i,len(grid[0])), (0,-1), grid, path)
        most_energized = max(len(set(path.values()))-1, most_energized)
    for col_i in range(len(grid[0])):
        path = {}
        moveBeam((-1,col_i), (1,0), grid, path)
        most_energized = max(len(set(path.values()))-1, most_energized)
        path = {}
        moveBeam((len(grid),col_i), (-1,0), grid, path)
        most_energized = max(len(set(path.values()))-1, most_energized)
    return most_energized

def moveBeam(pos, dir, grid, path):
    while not (pos, dir) in path.keys():
        path[(pos, dir)] = pos
        pos = tuple(map(lambda x,y: x+y, pos, dir))
        if pos[0] < 0 or pos[0] >= len(grid) or pos[1] < 0 or pos[1] >= len(grid[0]):
            return
        tile = grid[pos[0]][pos[1]]
        if tile == '/':
            dir = (dir[1]*-1,dir[0]*-1)
        elif tile == '\\':
            dir = (dir[1], dir[0])
        elif tile == '-':
            if dir[1] == 0:
                dir = (0,1)
                moveBeam(pos, (0,-1), grid, path)
        elif tile == '|':
            if dir[0] == 0:
                dir = (-1,0)
                moveBeam(pos, (1,0), grid, path)
    return

def parseData(line_list):
    grid = []
    for line in line_list:
        grid.append(list(line))
    return grid

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))