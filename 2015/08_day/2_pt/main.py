import sys

def solve(data):
    literal_len = 0
    decode_len = 0
    for line in data.split('\n'):
        literal_len += len(line)
        decode_len += len(encodeString(line))
    return decode_len - literal_len

def encodeString(string):
    decode_string = "\""
    i = 0
    while i < len(string):
        if string[i] == "\\":
            decode_string += "\\\\"
        elif string[i] == "\"":
            decode_string += "\\\""
        else:
            decode_string += string[i]
        i += 1
    return decode_string + "\""


if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
