import sys
import re

def parse_data(data):
    line_list = data.split('\n')
    registers = dict()
    registers['PC'] = 0
    registers['A'] = int(*re.findall('\d+', line_list[0]))
    registers['B'] = int(*re.findall('\d+', line_list[1]))
    registers['C'] = int(*re.findall('\d+', line_list[2]))
    program = list(map(int, re.findall('\d+', line_list[4])))
    return registers, program

def get_combo_operand(op, r):
    if 0 <= op <= 3:
        return op
    elif op == 4:
        return r['A']
    elif op == 5:
        return r['B']
    elif op == 6:
        return r['C']
    else:
        print("ERROR: Invalid combo operand %s" % (str(op)))
    return None

def dv(op, r, target):
    num = r['A']
    den = 1 << get_combo_operand(op, r)
    r[target] = num // den
    r['PC'] += 2

def adv(op, r):
    out = []
    dv(op, r, 'A')
    return out

def bxl(op, r):
    out = []
    r['B'] = r['B'] ^ op
    r['PC'] += 2
    return out

def bst(op, r):
    out = []
    r['B'] = get_combo_operand(op, r) % 8
    r['PC'] += 2
    return out

def jnz(op, r):
    out = []
    if r['A']:
        r['PC'] = op
    else:
        r['PC'] += 2
    return out

def bxc(op, r):
    out = []
    r['B'] = r['B'] ^ r['C']
    r['PC'] += 2
    return out

def out(op, r):
    out = []
    out.append(str(get_combo_operand(op, r) % 8))
    r['PC'] += 2
    return out

def bdv(op, r):
    out = []
    dv(op, r, 'B')
    return out

def cdv(op, r):
    out = []
    dv(op, r, 'C')
    return out

def solve(data):
    registers, program = parse_data(data)
    instructions = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]
    output = []
    while registers['PC'] < len(program):
        opcode = program[registers['PC']]
        operand = program[registers['PC']+1]
        output += instructions[opcode](operand, registers)
    return ','.join(output)

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
