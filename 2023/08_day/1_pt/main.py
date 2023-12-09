import sys

def main(data):
    instr_list, node_dict = parseData(data.split('\n'))
    step_count = 0
    instr_index = 0
    curr_node = "AAA"
    while curr_node != "ZZZ":
        curr_node = node_dict[curr_node][instr_list[instr_index]]
        instr_index = (instr_index + 1) % len(instr_list)
        step_count += 1
    return step_count

def parseData(line_list):
    instr_list = list(map(int, line_list[0].replace('L','0').replace('R','1')))
    node_dict = {}
    for i in range(2, len(line_list)):
        node_dict[line_list[i][0:3]] = (line_list[i][7:10], line_list[i][12:15])
    return (instr_list, node_dict)

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))
