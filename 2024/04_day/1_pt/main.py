import sys

def search(grid, i, j):
    directions = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
    word = "XMAS"
    word_count = 0
    for d in directions:
        next_i = i+d[0]
        next_j = j+d[1]
        word_index = 1
        while 0<=next_i<len(grid) and 0<=next_j<len(grid[0]) and word_index<4:
            if grid[next_i][next_j] == word[word_index]:
                word_index += 1
                next_i += d[0]
                next_j += d[1]
            else:
                break
        if word_index == 4:
            word_count += 1
    return word_count


def solve(data):
    grid = [list(line) for line in data.split('\n')]
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "X":
                total += search(grid, i, j)
    return total

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
