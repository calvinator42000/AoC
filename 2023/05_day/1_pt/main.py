import sys

def solve(data):
    seed_list, map_list = parse_maps(data.split('\n'))
    location_list = []
    for seed in seed_list:
        location_list.append(getSeedLocation(seed, map_list))
    return min(location_list)

def getSeedLocation(seed, map_list):
    curr_id = seed
    for next_map in map_list:
        for mapping in next_map:
            start_diff = curr_id - mapping[1]
            if start_diff >= 0 and start_diff < mapping[2]:
                curr_id = mapping[0] + start_diff
                break
    return curr_id

def parse_maps(line_list):
    seed_list = []
    map_list = []
    line_index = 0
    while line_index < len(line_list):
        if "seeds:" in line_list[line_index]:
            split_line = line_list[line_index].split(' ')
            for i in range(1,len(split_line)):
                seed_list.append(int(split_line[i]))
            line_index += 1
        elif "map:" in line_list[line_index]:
            line_index += 1
            next_map = []
            while line_index < len(line_list) and len(line_list[line_index]) > 0:
                next_map.append(tuple(map(int, line_list[line_index].split(' '))))
                line_index += 1
            map_list.append(next_map)
        line_index += 1
    return (seed_list, map_list)


if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
