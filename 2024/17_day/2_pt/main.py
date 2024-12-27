import sys
import re

def construct_a(program, program_i, A):
    if program_i == len(program):
        return A
    val = program[program_i]
    for i in range(8):
        B = A*8 + i
        if ((B >> (B % 8 ^ 1)) ^ B) % 8 ^ 7 == val:
            cand = construct_a(program, program_i+1, B)
            if cand != None:
                return cand
    return None

def solve(data):
    line_list = data.split('\n')
    program = list(map(int, re.findall('\d+', line_list[4])))
    A = construct_a(program[::-1], 0, 0)
    return A

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
