import sys

def main(data):
    literal_len = 0
    mem_len = 0
    for line in data.split('\n'):
        literal_len += len(line)
        mem_len += len(decodeString(line))
    return literal_len - mem_len

def decodeString(string):
    mem_string = ""
    i = 1
    while i < len(string)-1:
        if string[i] == "\\":
            i += 1
            if string[i] == "x":
                i += 2
                hex_string = bytes.fromhex(string[i-1:i+1])
                try:
                    mem_string += hex_string.decode("ASCII")
                except UnicodeDecodeError:
                    mem_string += "\ufffd"
            else:
                mem_string += string[i]
        else:
            mem_string += string[i]
        i += 1
    return mem_string


if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))
