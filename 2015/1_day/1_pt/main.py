import sys

def main(data):
    floor = 0
    for char in data:
        if char == '(':
            floor = floor + 1
        if char == ')':
            floor = floor - 1
    return floor

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read()))
