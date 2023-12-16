import sys

def main(data):
    pattern_list = parseData(data.split('\n'))
    note_sum = 0
    for pattern in pattern_list:
        num_col, num_row = findNewSplit(pattern)
        note_sum += num_col + 100*num_row
    return note_sum

def findNewSplit(pattern):
    old_splits = findSplits(pattern)
    new_pattern = [] + pattern
    for row_i in range(len(new_pattern)):
        for col_i in range(len(new_pattern[row_i])):
            changeSymbol(new_pattern, row_i, col_i)
            new_splits = findSplits(new_pattern)
            if new_splits != old_splits:
                for split in new_splits:
                    if not split in old_splits:
                        return split
            changeSymbol(new_pattern, row_i, col_i)
    return None

def changeSymbol(pattern, row_i, col_i):
    vals = ['.','#']
    pattern[row_i] = list(pattern[row_i])
    pattern[row_i][col_i] = vals[not vals.index(pattern[row_i][col_i])]
    pattern[row_i] = "".join(pattern[row_i])
    return pattern

def findSplits(pattern):
    splits = []
    refl_points = list(range(1,len(pattern[0])))
    for row in pattern:
        refl_points = getRefl(row, refl_points)
    if len(refl_points) > 0:
        for point in refl_points:
            splits.append((point, 0))
    refl_points = list(range(1,len(pattern)))
    for col in list(zip(*pattern)):
        refl_points = getRefl(col, refl_points)
    if len(refl_points) > 0:
        for point in refl_points:
            splits.append((0, point))
    return splits

def getRefl(line, refl_points):
    point_i = 0
    while point_i < len(refl_points):
        point = refl_points[point_i]
        left = line[:point][::-1]
        right = line[point:]
        refl_len = min(len(left), len(right))
        if right[:refl_len] != left[:refl_len]:
            refl_points.pop(point_i)
        else:
            point_i += 1
    return refl_points

def printPattern(pattern, num_col, num_row):
    output = ""
    if num_col > 0:
        output += " "*(num_col-1) + "><\n"
        for row in pattern:
            output += row + '\n'
        output += " "*(num_col-1) + "><\n"
    else:
        for i in range(len(pattern)):
            if i == num_row-1:
                output += f"v{pattern[i]}v\n"
            elif i == num_row:
                output += f"^{pattern[i]}^\n"
            else:
                output += f" {pattern[i]}\n"
    return output

def parseData(line_list):
    pattern_list = []
    curr_pattern = []
    for line in line_list:
        if len(line) == 0:
            pattern_list.append(curr_pattern)
            curr_pattern = []
        else:
            curr_pattern.append(line)
    pattern_list.append(curr_pattern)
    return pattern_list

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))
