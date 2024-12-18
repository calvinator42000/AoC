import sys

# Format is {<stone>: (<blinks_processed>, <processed_stones>)}
memo = dict()
blinks = 75

def blink(curr_stone):
    new_stones = None
    if curr_stone == '0':
        new_stones = ['1']
    elif len(curr_stone) % 2 == 0:
        new_stones = [str(int(curr_stone[:len(curr_stone)//2])), str(int(curr_stone[len(curr_stone)//2:]))]
    else:
        new_stones = [str(int(curr_stone)*2024)]
    return new_stones

def process_stones(curr_stone, blink_count):
    if (curr_stone, blink_count) in memo:
        return memo[(curr_stone, blink_count)]
    if blink_count == blinks:
        memo[(curr_stone, blink_count)] = 1
        return 1
    next_stones = blink(curr_stone)
    processed_stones_count = 0
    for stone in next_stones:
        processed_stones_count += process_stones(stone, blink_count+1)
    memo[(curr_stone, blink_count)] = processed_stones_count
    return processed_stones_count

def solve(data):
    stone_list = data.split()
    final_stone_count = 0
    for stone in stone_list:
        final_stone_count += process_stones(stone, 0)
    return final_stone_count

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
