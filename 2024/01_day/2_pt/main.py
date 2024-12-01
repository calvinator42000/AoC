import sys

def solve(data):
    line_list = data.split('\n')
    pair_list = [line.split() for line in line_list]
    left_list = [int(x[0]) for x in pair_list]
    right_list = [int(x[1]) for x in pair_list]
    result = 0
    for item in left_list:
        result += right_list.count(item)*item
    return result

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))