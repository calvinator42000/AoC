import sys
import numpy as np

directions = [(-1,0), (0,1), (1,0), (0,-1)]

class Plot:
    def __init__(self, label, row, col):
        self.label = label
        self.row = row
        self.col = col
        self.perim_lines = None
        self.region = None
    def update_region(self, farm):
        self.perim_lines = []
        for vert, horz in directions:
            next_row = self.row + vert
            next_col = self.col + horz
            if 0<=next_row<farm.shape[0] and 0<=next_col<farm.shape[1]:
                next_plot = farm[next_row,next_col]
                if next_plot.label != self.label:
                    self.perim_lines.append(dir)
                else:
                    if next_plot.region:
                        if next_plot.region != self.region:
                            next_plot.region += self.region
                            for plot in self.region:
                                if plot != self:
                                    plot.region = next_plot.region
                            self.region.clear()
                            self.region = next_plot.region
                    else:
                        self.region.append(next_plot)
                        next_plot.region = self.region
            else:
                self.perim_lines.append(dir)
        return self.perim_lines
    def __str__(self):
        return self.label
    def __repr__(self):
        return self.label

def create_regions(farm):
    region_list = []
    for row in farm:
        for plot in row:
            if plot.region == None:
                new_region = [plot]
                plot.region = new_region
                region_list.append(new_region)
            plot.update_region(farm)
    return region_list

def solve(data):
    farm = np.array([[Plot(item, i, j) for j,item in enumerate(row)] for i,row in enumerate(data.split('\n'))])
    region_list = list(map(tuple, create_regions(farm)))
    side_dict = dict.fromkeys(region_list, 0)
    # Doing north and south
    for i in range(farm.shape[0]):
        tracing_north = False
        tracing_south = False
        for j in range(farm.shape[1]):
            if not tracing_north:
                if i==0 or farm[i-1,j].label != farm[i,j].label:
                    side_dict[tuple(farm[i,j].region)] += 1
                    tracing_north = True
            elif i>0 and farm[i-1,j].label == farm[i,j].label:
                tracing_north = False
            if not tracing_south:
                if i==farm.shape[0]-1 or farm[i+1,j].label != farm[i,j].label:
                    side_dict[tuple(farm[i,j].region)] += 1
                    tracing_south = True
            elif i<farm.shape[0]-1 and farm[i+1,j].label == farm[i,j].label:
                tracing_south = False
            if j<farm.shape[1]-1 and farm[i,j+1].label != farm[i,j].label:
                tracing_north = False
                tracing_south = False
    # Doing east and west
    for j in range(farm.shape[1]):
        tracing_east = False
        tracing_west = False
        for i in range(farm.shape[0]):
            if not tracing_east:
                if j==farm.shape[1]-1 or farm[i,j+1].label != farm[i,j].label:
                    side_dict[tuple(farm[i,j].region)] += 1
                    tracing_east = True
            elif j<farm.shape[1]-1 and farm[i,j+1].label == farm[i,j].label:
                tracing_east = False
            if not tracing_west:
                if j==0 or farm[i,j-1].label != farm[i,j].label:
                    side_dict[tuple(farm[i,j].region)] += 1
                    tracing_west = True
            elif j>0 and farm[i,j-1].label == farm[i,j].label:
                tracing_west = False
            if i<farm.shape[0]-1 and farm[i+1,j].label != farm[i,j].label:
                tracing_east = False
                tracing_west = False
    total_price = 0
    for region in region_list:
        total_price += len(region) * side_dict[region]
    return total_price

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
