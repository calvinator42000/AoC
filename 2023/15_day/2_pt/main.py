import sys

def main(data):
    seq = data.split(',')
    box_dict = {}
    for i in range(256):
        box_dict[i] = []
    lense_dict = {}
    for inst in seq:
        if '=' in inst:
            lense = inst[:-2]
            val = int(inst[-1])
            box = get_hash(lense)
            if not lense in box_dict[box]:
                box_dict[box].append(lense)
            lense_dict[lense] = val
        elif '-' in inst:
            lense = inst[:-1]
            box = get_hash(lense)
            if lense in box_dict[box]:
                box_dict[box].remove(lense)
    total_focusing_power = 0
    for box in box_dict.keys():
        focusing_power = 0
        lense_list = box_dict[box]
        for i in range(len(lense_list)):
            focusing_power = 1 + box
            focusing_power = focusing_power * (i+1)
            focusing_power = focusing_power * lense_dict[lense_list[i]]
            total_focusing_power += focusing_power
    return total_focusing_power

def get_hash(string):
    curr_val = 0
    for char in string:
        curr_val += ord(char)
        curr_val = curr_val * 17
        curr_val = curr_val % 256
    return curr_val

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))