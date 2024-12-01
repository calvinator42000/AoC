import sys
import string

class Room:
    def __init__(self, line):
        checksum_start = line.index('[')
        self.checksum = line[checksum_start+1:-1]
        self.name = "".join(c for c in line[:checksum_start] if c.isalpha())
        self.id = int("".join(c for c in line[:checksum_start] if c.isdigit()))
    
    def is_real(self):
        frequency_rank = "".join(sorted(string.ascii_lowercase, key=lambda k: self.name.count(k), reverse=True))
        return frequency_rank[:5] == self.checksum

def solve(data):
    room_list = map(lambda line: Room(line), data.split('\n'))
    result = sum(room.id for room in room_list if room.is_real())
    return result

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
