import sys

def solve(data):
    inst_list = parseData(data.split('\n'))
    new_inst_list = convert_inst_list(inst_list)
    point_list, path_len = get_points(new_inst_list)
    sum = shoelace(point_list) + int(path_len/2) + 1
    return sum

def convert_inst_list(inst_list):
    new_inst_list = []
    for inst in inst_list:
        new_inst_list.append(convert_inst(inst[2][2:-1]))
    return new_inst_list

def convert_inst(code):
    dirs = 'RDLU'
    steps = int(code[:5],16)
    dir = dirs[int(code[5])]
    return (dir, steps)

def shoelace(point_list):
    prev_point = point_list[-1]
    sum = 0
    for point in point_list:
        sum += prev_point[0]*point[1] - prev_point[1]*point[0]
        prev_point = point
    return abs(int(sum/2))

def get_points(inst_list):
    dir_dict = {'U':(-1,0),'R':(0,1),'D':(1,0),'L':(0,-1)}
    point_list = []
    loc = (0,0)
    path_len = 0
    for inst in inst_list:
        dir, steps = inst
        dir_offset = dir_dict[dir]
        loc = (loc[0]+(dir_offset[0]*steps), loc[1]+(dir_offset[1]*steps))
        point_list.append(loc)
        path_len += steps
    return (point_list, path_len)

def parseData(line_list):
    inst_list = []
    for line in line_list:
        dir, steps, color = line.split(' ')
        inst_list.append((dir, int(steps), color))
    return inst_list

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
