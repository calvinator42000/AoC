import sys
import re

def solve(data):
    line_list = data.split('\n')
    time_list, dist_list = map(lambda x: list(map(int, list(re.findall(r'\d+', x)))), line_list)
    race_list = list(zip(time_list, dist_list))
    margin_mult = 1
    for race in race_list:
        margin_mult = margin_mult * sum(map(lambda x: (x*(race[0]-x)) > race[1], range(1,race[0])))
    return margin_mult

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
