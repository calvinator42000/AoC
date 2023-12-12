import sys

def main(data):
    x_rate = 1000000
    gal_list, rows_wo_gals, cols_wo_gals = getExpandedGalaxy(data.split('\n'))
    path_sum = 0
    for i in range(len(gal_list)):
        for j in range(i+1, len(gal_list)):
            x_row_space_count = [row for row in rows_wo_gals if row in list(range(min(gal_list[i][0],gal_list[j][0]), max(gal_list[i][0],gal_list[j][0])))]
            x_col_space_count = [col for col in cols_wo_gals if col in list(range(min(gal_list[i][1],gal_list[j][1]), max(gal_list[i][1],gal_list[j][1])))]
            path_sum += abs(gal_list[i][0]-gal_list[j][0])+(len(x_row_space_count)*(x_rate-1)) + abs(gal_list[i][1]-gal_list[j][1])+(len(x_col_space_count)*(x_rate-1))
    return path_sum

def getExpandedGalaxy(line_list):
    gal_list = []
    rows_wo_gals = []
    cols_wo_gals = list(range(len(line_list[0])))
    for row in range(len(line_list)):
        if line_list[row] == "."*len(line_list[row]):
            rows_wo_gals.append(row)
        else:
            for col in range(len(line_list[0])):
                if line_list[row][col] == '#':
                    gal_list.append((row,col))
                    try:
                        cols_wo_gals.remove(col)
                    except ValueError:
                        pass
    return (gal_list, rows_wo_gals, cols_wo_gals)


if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))
