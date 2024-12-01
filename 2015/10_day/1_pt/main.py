import sys

def solve(data):
    curr_num = data
    for i in range(40):
        curr_num = lookAndSay(curr_num)
    return len(curr_num)

def lookAndSay(num):
    output = ""
    last_digit = num[0]
    digit_count = 1
    for i in range(1, len(num)):
        if num[i] == last_digit:
            digit_count += 1
        else:
            output += str(digit_count) + last_digit
            last_digit = num[i]
            digit_count = 1 
    output += str(digit_count) + last_digit
    return output

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
