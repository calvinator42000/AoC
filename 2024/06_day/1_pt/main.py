import sys

def get_guard_pos(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Assuming guard always starts facing up
            if grid[i][j] == '^':
                return (i,j)
    return None

def take_step(grid, guard_pos, curr_dir):
    directions = [(-1,0), (0,1), (1,0), (0,-1)]
    next_step = tuple(map(sum, zip(guard_pos, directions[curr_dir])))
    if not (0<=next_step[0]<len(grid) and 0<=next_step[1]<len(grid[0])):
        return next_step, curr_dir
    # Assuming that the guard is not completely surrounded
    while grid[next_step[0]][next_step[1]] == '#':
        curr_dir = (curr_dir+1)%4
        next_step = tuple(map(sum, zip(guard_pos, directions[curr_dir])))
    return next_step, curr_dir

def count_pos(grid):
    pos_count = 0
    for line in grid:
        pos_count += line.count('X')
    return pos_count

def solve(data):
    grid = [list(line) for line in data.split('\n')]
    guard_pos = get_guard_pos(grid)
    curr_dir = 0
    while 0<=guard_pos[0]<len(grid) and 0<=guard_pos[1]<len(grid[0]):
        grid[guard_pos[0]][guard_pos[1]] = 'X'
        guard_pos, curr_dir = take_step(grid, guard_pos, curr_dir)
    return count_pos(grid)

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
