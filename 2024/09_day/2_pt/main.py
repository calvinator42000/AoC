import sys

class Block:
    def __init__(self, id, size, is_space):
        self.size = size
        self.is_space = is_space
        if self.is_space:
            self.id = -1
        else:
            self.id = id

def process_blocks(disk_map):
    block_list = []
    for i, size in enumerate(disk_map):
        block = Block(str(i//2), size, i%2==1)
        block = Block(i//2, size, i%2==1)
        block_list.append(block)
    return block_list

def checksum(disk):
    checksum = 0
    for i, id in enumerate(disk):
        if id >= 0:
            checksum += i*id
    return checksum

def compress_space(block_list):
    i = len(block_list)-1
    while i>=0:
        if not block_list[i].is_space:
            for j in range(i):
                if block_list[j].is_space and block_list[j].size >= block_list[i].size:
                    block_list[j].size -= block_list[i].size
                    new_space = Block(-1, block_list[i].size, True)
                    block_list.insert(j, block_list.pop(i))
                    block_list.insert(i, new_space)
                    break
        i -= 1
    # remove trailing space
    i = len(block_list)-1
    while block_list[i].id >= 0 and i >= 0: i-=1
    del block_list[i+1:]

def create_disk(block_list):
    disk = []
    for block in block_list:
        disk += [block.id] * block.size
    return disk

def solve(data):
    disk_map = list(map(int, data))
    block_list = process_blocks(disk_map)
    compress_space(block_list)
    disk = create_disk(block_list)
    return checksum(disk)

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
