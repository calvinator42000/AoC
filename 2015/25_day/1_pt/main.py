import sys

def main(data):
    ## (row, column)
    print(iterate(20151125))
    return 0

def iterate(num):
    return (num*252533) % 33554393

def parseData(data):
    parsed_line = data.split(' ')
    return (parsed_line[-3][:-1], parsed_line[-1][:-1])

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))

'''
row #, col 1
1 -> 1
2 -> 2
3 -> 4
4 -> 7
5 -> 11
6 -> 16
'''
