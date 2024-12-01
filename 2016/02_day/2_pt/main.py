import sys

def solve(data):
    data_lines = data.split('\n')
    num_pad = ((None,None,1,None,None),(None,2,3,4),(5,6,7,8,9),(None,'A','B','C',None),(None,None,'D',None,None))
    dirs = {'U':(-1,0),'R':(0,1),'D':(1,0),'L':(0,-1)}
    coord = (2,0)
    combination = ""
    for line in data_lines:
        for next_dir in line:
            coord_candidate = (max(0,coord[0]+dirs[next_dir][0]), max(0,coord[1]+dirs[next_dir][1]))
            try:
                num_candidate = num_pad[coord_candidate[0]][coord_candidate[1]]
                if num_candidate != None:
                    coord = coord_candidate
            except IndexError:
                continue
        combination += str(num_pad[coord[0]][coord[1]])
    return combination

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
