import sys

directions = [(-1,0), (0,1), (1,0), (0,-1)]

def follow_trail(trailhead, grid):
    visited = []
    queue = []
    queue.append(trailhead)
    score = 0
    while queue:
        step = queue.pop(0)
        if grid[step[0]][step[1]] == 9:
            score += 1
        else:
            for dir in directions:
                next_step = (step[0]+dir[0], step[1]+dir[1])
                if (not next_step in visited) and (0<=next_step[0]<len(grid) and 0<=next_step[1]<len(grid[0])):
                    if grid[next_step[0]][next_step[1]] == grid[step[0]][step[1]]+1:
                        queue.append(next_step)
                        visited.append(next_step)
    return score

def solve(data):
    grid = [list(map(int, line)) for line in data.split('\n')]
    trailhead_list = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                trailhead_list.append((i,j))
    total_score = 0
    for trailhead in trailhead_list:
        total_score += follow_trail(trailhead,grid)
    return total_score

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
