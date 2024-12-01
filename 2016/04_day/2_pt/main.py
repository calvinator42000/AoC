import sys
import string

class Room:
    def __init__(self, line):
        checksum_start = line.index('[')
        self.checksum = line[checksum_start+1:-1]
        self.id = int("".join(c for c in line[:checksum_start] if c.isdigit()))
        self.name = line[:checksum_start-len(str(self.id))-1]
    
    def is_real(self):
        frequency_rank = "".join(sorted(string.ascii_lowercase, key=lambda k: self.name.count(k), reverse=True))
        return frequency_rank[:5] == self.checksum
    
    def decrypt(self):
        alpha = string.ascii_lowercase
        plaintext = ""
        for c in self.name:
            if c=='-':
                plaintext += ' '
            else:
                plaintext += alpha[(alpha.index(c)+self.id)%26]
        return plaintext

def solve(data):
    room_list = map(lambda line: Room(line), data.split('\n'))
    decryptions = [[room.decrypt(), room.id] for room in room_list if room.is_real()]
    result = "\n".join(map(str,decryptions))
    return result

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
