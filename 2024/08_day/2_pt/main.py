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
    grid_height = len(line_list)
    grid_width = len(line_list[0])
    for frequency in antenna_dict:
        antenna_list = antenna_dict[frequency]
        antenna_pairs = itertools.combinations(antenna_list, 2)
        for antenna_a, antenna_b in antenna_pairs:
            height_diff = antenna_a[0] - antenna_b[0]
            width_diff = antenna_a[1] - antenna_b[1]
            curr_antinode = antenna_a
            while 0<=curr_antinode[0]<grid_height and 0<=curr_antinode[1]<grid_width:
                antinode_list.add(curr_antinode)
                curr_antinode = (curr_antinode[0]-height_diff, curr_antinode[1]-width_diff)
            curr_antinode = antenna_a
            while 0<=curr_antinode[0]<grid_height and 0<=curr_antinode[1]<grid_width:
                antinode_list.add(curr_antinode)
                curr_antinode = (curr_antinode[0]+height_diff, curr_antinode[1]+width_diff)
    return len(antinode_list)

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
