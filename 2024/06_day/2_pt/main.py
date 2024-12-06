import sys

directions = [(-1,0), (0,1), (1,0), (0,-1)]

def get_guard_pos(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Assuming guard always starts facing up
            if grid[i][j] == '^':
                return (i,j)
    return None
    

def take_step(grid, guard_pos, curr_dir):
    next_step = tuple(map(sum, zip(guard_pos, directions[curr_dir])))
    if not (0<=next_step[0]<len(grid) and 0<=next_step[1]<len(grid[0])):
        return next_step, curr_dir
    # Assuming that the guard is not completely surrounded
    while grid[next_step[0]][next_step[1]] == '#':
        curr_dir = (curr_dir+1)%4
        next_step = tuple(map(sum, zip(guard_pos, directions[curr_dir])))
    return next_step, curr_dir

def simulate_guard(grid):
    guard_pos = get_guard_pos(grid)
    curr_dir = 0
    pos_history = set()
    pos_dir_history = set()
    while 0<=guard_pos[0]<len(grid) and 0<=guard_pos[1]<len(grid[0]):
        pos_dir = (*guard_pos, curr_dir)
        if pos_dir in pos_dir_history:
            return pos_history, True
        pos_history.add(guard_pos)
        pos_dir_history.add(pos_dir)
        guard_pos, curr_dir = take_step(grid, guard_pos, curr_dir)
    return pos_history, False

def solve(data):
    grid = [list(line) for line in data.split('\n')]
    obstacle_candidates = set()
    pos_history, _ = simulate_guard(grid)
    for pos in pos_history:
        if grid[pos[0]][pos[1]] == '.':
            grid[pos[0]][pos[1]] = '#'
            _, loop_found = simulate_guard(grid)
            if loop_found:
                obstacle_candidates.add(pos)
            grid[pos[0]][pos[1]] = '.'
    return len(obstacle_candidates)

def print_grid(grid):
    for line in grid:
        print("".join(line))

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
