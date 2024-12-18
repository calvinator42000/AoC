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
        self.perim_lines = 0
        for vert, horz in directions:
            next_row = self.row + vert
            next_col = self.col + horz
            if 0<=next_row<farm.shape[0] and 0<=next_col<farm.shape[1]:
                next_plot = farm[next_row,next_col]
                if next_plot.label != self.label:
                    self.perim_lines += 1
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
                self.perim_lines += 1
        return self.perim_lines
    def __str__(self):
        return self.label
    def __repr__(self):
        return self.label

def solve(data):
    farm = np.array([[Plot(item, i, j) for j,item in enumerate(row)] for i,row in enumerate(data.split('\n'))])
    region_list = []
    for row in farm:
        for plot in row:
            if plot.region == None:
                new_region = [plot]
                plot.region = new_region
                region_list.append(new_region)
            plot.update_region(farm)
    total_price = 0
    for region in region_list:
        region_perimeter = 0
        for plot in region:
            region_perimeter += plot.perim_lines
        total_price += len(region) * region_perimeter
    return total_price

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
