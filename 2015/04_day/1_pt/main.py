import sys
import hashlib

def solve(key):
    solution = 1
    while True:
        if check_hash(get_hash(bytes(key+str(solution),'utf-8'))):
            break
        solution = solution + 1
    return solution

def get_hash(key_in):
    return hashlib.md5(key_in)

def check_hash(h):
    return h.hexdigest()[:5] == '00000'

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
