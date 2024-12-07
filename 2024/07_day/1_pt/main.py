import sys
import itertools

def evaluation(expression):
    val = expression[0]
    for i in range(1, len(expression), 2):
        operator = expression[i]
        operand = expression[i+1]
        val = eval(str(val) + operator + operand)
    return val

def is_valid(val, operands):
    operators = ['+', '*']
    num_pos = len(operands)-1
    config_list = list(itertools.product(operators, repeat=num_pos))
    for config in config_list:
        expression = [''] * (len(operands) + num_pos)
        expression[::2] = operands
        expression[1::2] = config
        if evaluation(expression) == val:
            return True
    return False

def solve(data):
    equations = parse_data(data)
    total = 0
    for val in equations:
        operands = equations[val]
        if is_valid(val, operands):
            total += val
    return total

def parse_data(data):
    line_list = [line.split() for line in data.split('\n')]
    equations = dict()
    for line in line_list:
        equations[int(line[0][:-1])] = line[1:]
    return equations

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
