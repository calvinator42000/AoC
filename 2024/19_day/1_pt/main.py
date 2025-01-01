import sys

def parse_data(data):
    line_list = data.split('\n')
    pattern_list = line_list[0].split(', ')
    design_list = line_list[2:]
    return pattern_list, design_list

def get_designs(design, pattern_list, memo):
    if design in memo:
        return memo[design]
    for pattern in pattern_list:
        if design.startswith(pattern):
            if get_designs(design[len(pattern):], pattern_list, memo):
                memo[design] = True
                return True
    return False

def solve(data):
    pattern_list, design_list = parse_data(data)
    possible_design_count = 0
    memo = {"":True}
    for design in design_list:
        possible_design_count += get_designs(design, pattern_list, memo)
    return possible_design_count

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
