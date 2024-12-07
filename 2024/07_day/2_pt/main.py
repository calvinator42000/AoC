import sys

operator_list = ['+', '*', '']

# Backtracking
# I originally just kept my strategy for pt1 and let it run for a few minutes
# but I wanted to try this implementation after the fact.
def is_valid(val, operand_list, operand_index, result):
    if operand_index == len(operand_list):
        return result == val
    if result > val:
        return False
    for operator in operator_list:
        expression = str(result) + operator + operand_list[operand_index]
        new_result = eval(expression)
        if is_valid(val, operand_list, operand_index+1, new_result):
            return True
    return False

def solve(data):
    equations = parse_data(data)
    total = 0
    i = 0
    for val in equations:
        print(i)
        operand_list = equations[val]
        if is_valid(val, operand_list, 1, int(operand_list[0])):
            total += val
        i += 1
    return total

def parse_data(data):
    line_list = [line.split() for line in data.split('\n')]
    equations = dict()
    for line in line_list:
        equations[int(line[0][:-1])] = line[1:]
    return equations

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
