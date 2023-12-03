import sys

def main(data):
    lines = data.split('\n')
    gears = {}
    row = 0
    while row < len(lines):
        col = 0
        while col < len(lines[row]):
            if lines[row][col].isdigit():
                num = getNum(lines[row], col)
                surr_coords = getSurrCoords(row, col, len(num), len(lines), len(lines[row]))
                for coord in surr_coords:
                    char = lines[coord[0]][coord[1]]
                    if char == '*':
                        if not coord in list(gears.keys()):
                            gears[coord] = []
                        gears[coord].append(int(num))
                col += len(num)
            col += 1
        row += 1
    gear_sum = 0
    for gear in gears.keys():
        if len(gears[gear]) == 2:
            gear_sum += (gears[gear][0] * gears[gear][1])
    return gear_sum

def getSurrCoords(row, start, length, max_row, max_col):
    coords = []
    for i in range(start-1, start+length+1):
        coords.append((row-1, i))
        coords.append((row+1, i))
    coords.append((row, start-1))
    coords.append((row, start+length))
    valid_coords = []
    for coord in coords:
        if not (coord[0]<0 or coord[0]>=max_row or coord[1]<0 or coord[1]>=max_col):
            valid_coords.append(coord)
    return valid_coords

def getNum(line, start):
    num = ""
    for col in range(start, len(line)):
        if line[col].isdigit():
            num += line[col]
        else:
            break
    return num

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))
