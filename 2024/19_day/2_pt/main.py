import sys

def parse_data(data):
    line_list = data.split('\n')
    pattern_list = line_list[0].split(', ')
    design_list = line_list[2:]
    return pattern_list, design_list

def get_designs(design, pattern_list, memo):
    if design in memo:
        return memo[design]
    if len(design) == 0:
        return 1
    design_count = 0
    for pattern in pattern_list:
        if design.startswith(pattern):
            design_count += get_designs(design[len(pattern):], pattern_list, memo)
            memo[design] = design_count
    return design_count

def solve(data):
    pattern_list, design_list = parse_data(data)
    possible_design_count = 0
    memo = dict()
    for design in design_list:
        possible_design_count += get_designs(design, pattern_list, memo)
    return possible_design_count

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
