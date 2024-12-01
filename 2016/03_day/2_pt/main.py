import sys

def is_triangle(triangle):
    a,b,c=triangle
    return a+b>c and a+c>b and b+c>a

def parse_data(data):
    line_list = [list(map(int,line.split())) for line in data.split('\n')]
    triangle_list = []
    for i in range(0, len(line_list), 3):
        for j in range(3):
            triangle = (line_list[i][j], line_list[i+1][j], line_list[i+2][j])
            triangle_list.append(triangle)
    return triangle_list

def solve(data):
    triangle_list = parse_data(data)
    result = sum(map(is_triangle, triangle_list))
    return result

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
