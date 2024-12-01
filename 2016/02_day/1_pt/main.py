import sys

def solve(data):
    data_lines = data.split('\n')
    num_pad = ((1,2,3),(4,5,6),(7,8,9))
    dirs = {'U':(-1,0),'R':(0,1),'D':(1,0),'L':(0,-1)}
    coord = (1,1)
    combination = ""
    for line in data_lines:
        for next_dir in line:
            coord_candidate = (max(0,coord[0]+dirs[next_dir][0]), max(0,coord[1]+dirs[next_dir][1]))
            try:
                num_pad[coord_candidate[0]][coord_candidate[1]]
                coord = coord_candidate
            except IndexError:
                continue
        combination += str(num_pad[coord[0]][coord[1]])
    return combination

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
