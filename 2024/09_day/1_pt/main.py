import sys

def checksum(blocks):
    return sum(i*int(val) for i,val in enumerate(blocks))

def solve(data):
    disk_map = list(map(int, data))
    blocks = []
    for i in range(len(disk_map)):
        if i%2:
            for j in range(disk_map[i]):
                blocks.append('')
        else:
            for j in range(disk_map[i]):
                blocks.append(str(i//2))
    i = 0
    while i < len(blocks):
        if not blocks[i]:
            while not blocks[-1]:
                blocks.pop(-1)
            if i >= len(blocks):
                break
            blocks[i] = blocks.pop(-1)
        i += 1
    return checksum(blocks)

def print_blocks(blocks):
    for b in blocks:
        if b: print(b,end='')
        else: print(' ',end='')
    print()

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
