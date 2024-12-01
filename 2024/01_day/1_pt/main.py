import sys

def solve(data):
    line_list = data.split('\n')
    pair_list = [line.split() for line in line_list]
    left_list = sorted(int(x[0]) for x in pair_list)
    right_list = sorted(int(x[1]) for x in pair_list)
    new_pairs = list(zip(left_list, right_list))
    result = 0
    for x,y in new_pairs:
        result += abs(x-y)
    return result

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))