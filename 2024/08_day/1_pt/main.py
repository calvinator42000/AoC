import sys
import re
import itertools

def get_antennas(line_list):
    antenna_dict = dict()
    for line_index in range(len(line_list)):
        for match in re.finditer("[^\.]", line_list[line_index]):
            frequency = line_list[line_index][match.start()]
            if not frequency in antenna_dict:
                antenna_dict[frequency] = []
            antenna_dict[frequency].append((line_index, match.start()))
    return antenna_dict

def solve(data):
    line_list = data.split('\n')
    antenna_dict = get_antennas(line_list)
    antinode_list = set()
    for frequency in antenna_dict:
        antenna_list = antenna_dict[frequency]
        antenna_pairs = itertools.combinations(antenna_list, 2)
        for antenna_a, antenna_b in antenna_pairs:
            antinode_a = (antenna_a[0]*2-antenna_b[0], antenna_a[1]*2-antenna_b[1])
            antinode_b = (antenna_b[0]*2-antenna_a[0], antenna_b[1]*2-antenna_a[1])
            for antinode in (antinode_a, antinode_b):
                if 0<=antinode[0]<len(line_list) and 0<=antinode[1]<len(line_list[0]):
                    antinode_list.add(antinode)
    return len(antinode_list)

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
