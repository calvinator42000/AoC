import sys

def is_triangle(triangle):
    a,b,c=triangle
    return a+b>c and a+c>b and b+c>a

def solve(data):
    triangle_list = [list(map(int,line.split())) for line in data.split('\n')]
    result = sum(map(is_triangle, triangle_list))
    return result

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
