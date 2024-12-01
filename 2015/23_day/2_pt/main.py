import sys

def solve(data):
    inst_list = parseData(data.split('\n'))
    inst_ptr = 0
    regs = {'a': 1, 'b': 0}
    while inst_ptr < len(inst_list):
        inst = inst_list[inst_ptr]
        if inst[0] == "hlf":
            regs[inst[1]] = int(regs[inst[1]] / 2)
            inst_ptr += 1
        elif inst[0] == "tpl":
            regs[inst[1]] = regs[inst[1]] * 3
            inst_ptr += 1
        elif inst[0] == "inc":
            regs[inst[1]] += 1
            inst_ptr += 1
        elif inst[0] == "jmp":
            inst_ptr += inst[1]
        elif inst[0] == "jie":
            if regs[inst[1][0]] % 2 == 0:
                inst_ptr += inst[2]
            else:
                inst_ptr += 1
        elif inst[0] == "jio":
            if regs[inst[1][0]] == 1:
                inst_ptr += inst[2]
            else:
                inst_ptr += 1
    return regs['b']

def parseData(data_list):
    inst_list = []
    for line in data_list:
        parsed_line = line.split(' ')
        if len(parsed_line) == 2:
            if parsed_line[0] == "jmp":
                inst_list.append((parsed_line[0], int(parsed_line[1])))
            else:
                inst_list.append(tuple(parsed_line))
        elif len(parsed_line) == 3:
            inst_list.append((parsed_line[0], parsed_line[1][0], int(parsed_line[2])))
    return inst_list


if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
