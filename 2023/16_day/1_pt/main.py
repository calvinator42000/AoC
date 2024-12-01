import sys

def solve(data):
    grid = parseData(data.split('\n'))
    path = {}
    moveBeam((0,-1), (0,1), grid, path)    
    energized_list = set(path.values())
    return len(energized_list)-1

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
    print(solve(open(sys.argv[1]).read().rstrip()))