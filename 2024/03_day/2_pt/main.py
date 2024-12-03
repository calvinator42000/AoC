import sys
import re

def mul(x,y):
    return x*y

def solve(data):
    regex = r'(?:(mul\([0-9]{1,3},[0-9]{1,3}\))|(do\(\))|(don\'t\(\)))'
    ops = re.findall(regex, data)
    result = 0
    do = True
    for op in ops:
        if op[0] and do:
            result += eval(op[0])
        elif op[1]:
            do = True
        elif op[2]:
            do = False
    return result

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
