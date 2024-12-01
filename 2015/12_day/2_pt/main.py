import sys

def solve(data):
    if data[0] == '{':
        num_sum = getObjectSum(data, 1, False)[0]
    elif data[0] == '[':
        num_sum = getListSum(data, 1)[0]
    return num_sum

def getObjectSum(data, index, red_flag):
    obj_sum = 0
    in_list = False
    while data[index] != '}':
        if data[index] == '{':
            new_sum, index = getObjectSum(data, index+1, red_flag)
            obj_sum += new_sum
        elif data[index] == '[':
            new_sum, index = getListSum(data, index+1)
            obj_sum += new_sum
        elif data[index: index+3] == "red":
            red_flag = True
            index += 3
        elif data[index].isnumeric():
            num = data[index]
            if data[index-1] == '-':
                num = '-' + num
            while data[index+1].isnumeric():
                index += 1
                num += data[index]
            obj_sum += int(num)
            index += 1
        else:
            index += 1
    if red_flag:
        obj_sum = 0
    return (obj_sum, index+1)

def getListSum(data, index):
    list_sum = 0
    while data[index] != ']':
        if data[index] == '{':
            new_sum, index = getObjectSum(data, index+1, False)
            list_sum += new_sum
        elif data[index] == '[':
            new_sum, index = getListSum(data, index+1)
            list_sum += new_sum
        elif data[index].isnumeric():
            num = data[index]
            if data[index-1] == '-':
                num = '-' + num
            while data[index+1].isnumeric():
                index += 1
                num += data[index]
            list_sum += int(num)
            index += 1
        else:
            index += 1
    return (list_sum, index+1)


if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
