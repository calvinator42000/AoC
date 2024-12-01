import sys
import math

def solve(data):
    starting_node_list, instr_list, node_dict = parseData(data.split('\n'))
    step_count_list = []
    for node in starting_node_list:
        step_count = 0
        instr_index = 0
        curr_node = node
        while curr_node[2] != 'Z':
            curr_node = node_dict[curr_node][instr_list[instr_index]]
            instr_index = (instr_index + 1) % len(instr_list)
            step_count += 1
        step_count_list.append(step_count)
    return math.lcm(*step_count_list)

def parseData(line_list):
    instr_list = list(map(int, line_list[0].replace('L','0').replace('R','1')))
    node_dict = {}
    starting_node_list = []
    for i in range(2, len(line_list)):
        node_dict[line_list[i][0:3]] = (line_list[i][7:10], line_list[i][12:15])
        if line_list[i][2] == 'A':
            starting_node_list.append(line_list[i][0:3])
    return (starting_node_list, instr_list, node_dict)

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
