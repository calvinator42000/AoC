import sys

def main(data):
    seq = data.split(',')
    hash_sum = 0
    for inst in seq:
        hash_sum += get_hash(inst)
    return hash_sum

def get_hash(string):
    curr_val = 0
    for char in string:
        curr_val += ord(char)
        curr_val = curr_val * 17
        curr_val = curr_val % 256
    return curr_val

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))
