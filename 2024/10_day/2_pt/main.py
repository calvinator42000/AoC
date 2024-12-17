import sys

directions = [(-1,0), (0,1), (1,0), (0,-1)]

def follow_trail(path, grid):
    curr_pos = path[-1]
    rating = 0
    if grid[curr_pos[0]][curr_pos[1]] == 9:
        return 1
    for dir in directions:
        next_step = (curr_pos[0]+dir[0], curr_pos[1]+dir[1])
        if 0<=next_step[0]<len(grid) and 0<=next_step[1]<len(grid[0]):
            if grid[next_step[0]][next_step[1]] == grid[curr_pos[0]][curr_pos[1]]+1:
                rating += follow_trail(path + [next_step], grid)
    return rating

def solve(data):
    grid = [list(map(int, line)) for line in data.split('\n')]
    trailhead_list = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                trailhead_list.append((i,j))
    total_rating = 0
    for trailhead in trailhead_list:
        total_rating += follow_trail([trailhead], grid)
    return total_rating

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
