import sys
import re

def solve(data):
    row_data_list = parseData(data.split('\n'))
    com_sum = 0
    for row_data in row_data_list:
        row, group_list = row_data
        q_loc_list = [val.start(0) for val in re.finditer(r'\?',row)]
        com_sum += len(getValidCom(row, group_list, q_loc_list))
    return com_sum

def getValidCom(row, group_list, q_loc_list, curr_index = 0, valid_list = []):
    if curr_index < len(q_loc_list):
        q_loc = q_loc_list[curr_index]
        if row[q_loc] == '?':
            row = row[:q_loc] + '#' + row[q_loc+1:]
            val_results = isValid(row, group_list)
            if val_results == 2:
                valid_list = getValidCom(row, group_list, q_loc_list, curr_index+1, valid_list)
            elif val_results == 1:
                if not row in valid_list:
                    valid_list = [row] + valid_list
            row = row[:q_loc] + '.' + row[q_loc+1:]
            val_results = isValid(row, group_list)
            if val_results == 2:
                valid_list = getValidCom(row, group_list, q_loc_list, curr_index+1, valid_list)
            elif val_results == 1:
                if not row in valid_list:
                    valid_list = [row] + valid_list
        curr_index += 1
    return valid_list


def isValid(row, group_list):
    if '?' in row:
        return 2
    found_groups = [x for x in row.split('.') if len(x) > 0]
    if len(found_groups) != len(group_list):
        return 0
    for group_index in range(len(group_list)):
        if len(found_groups[group_index]) != group_list[group_index]:
            return 0
    return 1

def parseData(line_list):
    row_data_list = []
    for line in line_list:
        split_line = line.split(' ')
        row_data_list.append((split_line[0], list(map(int, split_line[1].split(',')))))
    return row_data_list


if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
