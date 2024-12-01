import sys
import re

def solve(data):
    strings = data.split('\n')
    nice_count = 0
    for s in strings:
        if check_str(s):
            nice_count = nice_count + 1
    return nice_count

def check_str(string):
    return check_pairs(string) and \
            check_sandwich(string)

def check_pairs(string):
    valid = re.compile(r".*(..).*\1")
    return valid.match(string) != None

def check_sandwich(string):
    valid = re.compile(r".*(.).\1")
    return valid.match(string) != None

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read()))
