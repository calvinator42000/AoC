import sys

def main(data):
    ribbon = 0
    for line in data.split('\n'):
        if len(line) > 0:
            line = [int(x) for x in line.split('x')]
            line.sort()
            a,b,c = tuple(line)
            ribbon = ribbon + (2*a + 2*b) + (a*b*c)
    return ribbon

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read()))
