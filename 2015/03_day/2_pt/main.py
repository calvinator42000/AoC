import sys

def solve(data):
    house_list = []
    coords = [(0,0), (0,0)]
    house_list.append((0,0))
    turn = True
    x = 0
    y = 0
    for direction in data:
        x,y = coords[turn]
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
        coords[turn] = (x,y)
        turn = not turn
    return len(house_list)

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read()))
