import sys

def solve(data):
    new_str = ""
    for char in data:
        if char == '{' or char == '}' or char == '[' or char == ']':
            new_str += char
    return new_str

if __name__ == "__main__":
    open('test_input4', 'w').write(solve(open(sys.argv[1]).read().rstrip()))
