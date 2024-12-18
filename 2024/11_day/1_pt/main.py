import sys

def blink(stone_list):
    new_stone_list = []
    for i in range(len(stone_list)):
        stone = stone_list[i]
        if stone == '0':
            new_stone_list.append('1')
        elif len(stone) % 2 == 0:
            new_stone_list.append(str(int(stone[:len(stone)//2])))
            new_stone_list.append(str(int(stone[len(stone)//2:])))
        else:
            new_stone_list.append(str(int(stone)*2024))
    return new_stone_list

def solve(data):
    stone_list = data.split()
    blinks = 25
    for i in range(blinks):
        stone_list = blink(stone_list)
    return len(stone_list)

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
