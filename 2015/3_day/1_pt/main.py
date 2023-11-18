import sys

def main(data):
    house_list = []
    x = 0
    y = 0
    house_list.append((x,y))
    for direction in data:
        if direction == '^':
            y = y + 1
        elif direction == 'v':
            y = y - 1
        elif direction == '>':
            x = x + 1
        elif direction == '<':
            x = x - 1
        if not (x,y) in house_list:
            house_list.append((x,y))
    return len(house_list)

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read()))
