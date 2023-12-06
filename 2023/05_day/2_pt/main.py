import sys

def main(data):
    seed_range_list, map_list = parse_maps(data.split('\n'))
    location_ranges = []
    for seed_range in seed_range_list:
        location_ranges += getSeedLocation((seed_range[0],seed_range[0]+seed_range[1]), map_list)
    return sorted(location_ranges, key=lambda x: x[0])[0][0]

def getSeedLocation(in_range, map_list, map_list_index = 0):
    if map_list_index >= len(map_list):
        return [in_range]
    proc_range_list = [in_range]
    next_range_list = []
    for mapping in map_list[map_list_index]:
        curr_range_list = [] + proc_range_list
        proc_range_list = []
        for curr_range in curr_range_list:
            start = curr_range[0]
            end = curr_range[1]
            map_diff = mapping[0] - mapping[1]
            inner_start = max(start, mapping[1])
            inner_end = min(end, mapping[1] + mapping[2])
            left_start = start
            left_end = min(end, inner_start)
            right_start = max(start, inner_end)
            right_end = end
            range_candidates = [(inner_start+map_diff,inner_end+map_diff), (left_start,left_end), (right_start,right_end)]
            for i in range(len(range_candidates)):
                if range_candidates[i][1] - range_candidates[i][0] > 0:
                    if i == 0:
                        next_range_list += getSeedLocation(range_candidates[i], map_list, map_list_index+1)
                    else:
                        proc_range_list.append(range_candidates[i])
    for proc_range in proc_range_list:
        next_range_list += getSeedLocation(proc_range, map_list, map_list_index+1)
    return next_range_list

def parse_maps(line_list):
    seed_range_list = []
    map_list = []
    line_index = 0
    while line_index < len(line_list):
        if "seeds:" in line_list[line_index]:
            ranges = line_list[line_index].split(' ')[1:]
            range_index = 0
            while range_index < len(ranges):
                start = int(ranges[range_index])
                length = int(ranges[range_index+1])
                seed_range_list.append((start, length))
                range_index += 2
            line_index += 1
        elif "map:" in line_list[line_index]:
            line_index += 1
            next_map = []
            while line_index < len(line_list) and len(line_list[line_index]) > 0:
                next_map.append(tuple(map(int, line_list[line_index].split(' '))))
                line_index += 1
            map_list.append(next_map)
        line_index += 1
    return (seed_range_list, map_list)


if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))
