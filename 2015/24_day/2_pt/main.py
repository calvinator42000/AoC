import sys
import math

def main(data):
    pkg_list = parseData(data.split('\n'))
    possible_groups = sorted(list(getPossibleGroups(pkg_list, int(sum(pkg_list)/4))), key=lambda x: len(x))
    min_group_size = len(possible_groups[0])
    group1_candidates = []
    for group in possible_groups:
        if len(group) == min_group_size:
            group1_candidates.append(group)
    group1_candidates.sort(key=lambda x: math.prod(x))
    return math.prod(group1_candidates[0])

def getPossibleGroups(pkg_list, sum_goal, curr_config = [], curr_sum = 0):
    if curr_sum == sum_goal:
        yield curr_config
    if curr_sum > sum_goal:
        return
    for i in range(len(pkg_list)):
        yield from getPossibleGroups(pkg_list[i+1:], sum_goal, curr_config + [pkg_list[i]], curr_sum + pkg_list[i])

def parseData(data_list):
    pkg_list = []
    for line in data_list:
        pkg_list.append(int(line))
    return sorted(pkg_list, reverse=True)

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))
