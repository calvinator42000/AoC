import sys

def solve(data):
    coords = parseData(data)
    return simulate(20151125,coords[0],coords[1])

def simulate(start, row, col):
    num_iter = findCode(row, col)-1
    num = start
    for i in range(num_iter):
        num = iterate(num)
    return num

def findCode(row, col):
    return col + sum(range(row+col-1))

def iterate(num):
    return (num*252533) % 33554393

def parseData(data):
    parsed_line = data.split(' ')
    return (int(parsed_line[-3][:-1]), int(parsed_line[-1][:-1]))

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
