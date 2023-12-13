import sys

def main(data):
    row_data_list = parseData(data.split('\n'))
    com_sum = 0
    for row_data in row_data_list:
        sol_cache = {}
        row, group_list = row_data
        row = row + '?' + row + '?' + row + '?' + row + '?' + row
        group_list = group_list*5
        com_sum += getValidCom(row, group_list, sol_cache)
    return com_sum

def getValidCom(row, group_list, sol_cache, row_i=0, group_i=0, curr_group_len=0):
    sol_key = (row_i, group_i, curr_group_len)
    if sol_key in sol_cache.keys():
        return sol_cache[sol_key]
    if row_i == len(row):
        return isValid(group_list, group_i, curr_group_len)
    else:
        count = 0
        for change in ['#','.']:
            if row[row_i] == change or row[row_i] == '?':
                if change == '#':
                    count += getValidCom(row, group_list, sol_cache, row_i+1, group_i, curr_group_len+1)
                elif curr_group_len == 0:
                    count += getValidCom(row, group_list, sol_cache, row_i+1, group_i, 0)
                elif group_i < len(group_list) and curr_group_len == group_list[group_i]:
                    count += getValidCom(row, group_list, sol_cache, row_i+1, group_i+1, 0)
        sol_cache[sol_key] = count
        return count

def isValid(group_list, group_i, curr_group_len):
    if group_i == len(group_list) and curr_group_len == 0:
        return 1
    elif group_i == len(group_list)-1 and curr_group_len == group_list[group_i]:
        return 1
    else:
        return 0

def parseData(line_list):
    row_data_list = []
    for line in line_list:
        split_line = line.split(' ')
        row_data_list.append((split_line[0], list(map(int, split_line[1].split(',')))))
    return row_data_list

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))
