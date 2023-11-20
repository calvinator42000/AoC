import sys

grid_size = 1000

def main(data):
    grid = [[0 for i in range(grid_size)] for j in range(grid_size)]
    lines = data.split('\n')
    for l in lines:
        cmd = parse_line(l)
        for i in range(cmd[1][0],cmd[2][0]+1):
            for j in range(cmd[1][1],cmd[2][1]+1):
                if cmd[0] == "off":
                    if not grid[i][j] == 0:
                        grid[i][j] = grid[i][j] - 1
                elif cmd[0] == "on":
                    grid[i][j] = grid[i][j] + 1
                elif cmd[0] == "toggle":
                    grid[i][j] = grid[i][j] + 2
                else:
                    print("ERROR: Command not recognized '%s'", str(cmd))
    return count_brightness(grid)

def count_brightness(grid):
    brightness = 0
    for i in range(grid_size):
        for j in range(grid_size):
            brightness = brightness + grid[i][j]
    return brightness

def parse_line(line):
    ## Command (Operation, Coords1, Coords2)
    cmd = (None,None,None)
    args = line.split(" ")
    if args[0] == "turn":
        cmd = (args[1], \
                tuple(map(int,args[2].split(','))), \
                tuple(map(int,args[4].split(','))))
    elif args[0] == "toggle":
        cmd = (args[0], \
                tuple(map(int,args[1].split(','))), \
                tuple(map(int,args[3].split(','))))
    return cmd

def print_grid(grid):
    output = ""
    for row in grid:
        for light in row:
            output = output + str(light) + ' '
        output = output + '\n'
    print(output)

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))
