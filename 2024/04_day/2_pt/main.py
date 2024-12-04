import sys

def valid(grid, i, j):
    directions = [(1,1),(-1,1),(-1,-1),(1,-1)]
    chars = ""
    for d in directions:
        next_i = i+d[0]
        next_j = j+d[1]
        if not (0<=next_i<len(grid) and 0<=next_j<len(grid[0])):
            return False
        chars += grid[next_i][next_j]
    candidates = ["SSMM","SMMS","MMSS","MSSM"]
    if chars in candidates:
        return True
    else:
        return False

def solve(data):
    grid = [list(line) for line in data.split('\n')]
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "A":
                total += valid(grid, i, j)
    return total

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
