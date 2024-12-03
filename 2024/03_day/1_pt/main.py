import sys
import re

def mul(x,y):
    return x*y

def solve(data):
    ops = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', data)
    result = 0
    for op in ops:
        result += eval(op)
    return result

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
