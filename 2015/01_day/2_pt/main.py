import sys

def solve(data):
    floor = 0
    i = 0
    while floor >= 0:
        char = data[i]
        if char == '(':
            floor = floor + 1
        if char == ')':
            floor = floor - 1
        i = i + 1
    return i

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read()))
