import sys

def main(data):
    num_sum = 0
    negative = False
    index = 0
    while index < len(data):
        if data[index].isnumeric():
            num = data[index]
            if data[index-1] == '-':
                num = '-' + num
            index += 1
            while data[index].isnumeric():
                num += data[index]
                index += 1
            num_sum += int(num)
        else:
            index += 1
    return num_sum

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))
