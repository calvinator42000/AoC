import sys

def solve(data):
    paper = 0
    for line in data.split('\n'):
        if len(line) > 0:
            line = [int(x) for x in line.split('x')]
            line.sort()
            a,b,c = tuple(line)
            paper = paper + 2*(a*b + a*c + b*c) + (a*b)
    return paper

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read()))
