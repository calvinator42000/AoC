import sys

def main(data):
    directions = data.split(", ")
    dirs = ((0,1),(1,0),(0,-1),(-1,0))
    coord = (0,0)
    dir_index = 0
    for next_dir in directions:
        if next_dir[0] == 'L':
            dir_index = (dir_index-1) % 4
        elif next_dir[0] == 'R':
            dir_index = (dir_index+1) % 4
        coord = (coord[0]+(dirs[dir_index][0]*int(next_dir[1:])), coord[1]+(dirs[dir_index][1]*int(next_dir[1:])))
    return abs(coord[0]) + abs(coord[1])

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))
