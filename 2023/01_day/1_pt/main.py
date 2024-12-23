import sys
import re

def solve(data):
    num_sum = 0
    for line in data.split('\n'):
        num_sum += int("".join([re.findall(r'\d', line)[num] for num in (0,-1)]))
    return num_sum

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
