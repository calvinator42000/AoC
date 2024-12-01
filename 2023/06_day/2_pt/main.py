import sys
import re

def solve(data):
    line_list = data.split('\n')

    race = tuple(map(lambda x: int(re.findall(r'\d+', x.replace(' ',''))[0]), line_list))
    print(race)
    return sum(map(lambda x: (x*(race[0]-x)) > race[1], range(1,race[0])))

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
