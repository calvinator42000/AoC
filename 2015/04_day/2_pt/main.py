import sys
import hashlib

def main(key):
    solution = 1
    while True:
        if check_hash(get_hash(bytes(key+str(solution),'utf-8'))):
            break
        solution = solution + 1
    return solution

def get_hash(key_in):
    return hashlib.md5(key_in)

def check_hash(h):
    return h.hexdigest()[:6] == '000000'

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))
