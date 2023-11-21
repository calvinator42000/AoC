import sys

class Grid:
    def __init__(self, grid_data):
        self.grid = self.parseData(grid_data)
        self.setNeighbors()

    def update(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                self.grid[i][j].update()
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                self.grid[i][j].updateNeighborsOn()

    def countLights(self):
        count = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                if self.grid[i][j].state:
                    count += 1
        return count

    def parseData(self, grid_data):
        line_list = grid_data.split('\n')
        grid = [[None for i in range(len(line_list))] for j in range(len(line_list))]
        for i in range(len(line_list)):
            light_list = list(line_list[i])
            for j in range(len(light_list)):
                new_light = Light(light_list[j] == '#', [])
                if (i==0 and j==0) or (i==0 and j==(len(light_list)-1)) or (i==(len(line_list)-1) and j==0) or (i==(len(line_list)-1) and j==(len(light_list)-1)):
                    new_light.is_corner = True
                    new_light.state = True
                grid[i][j] = new_light
        return grid

    def setNeighbors(self):
        offset_list = [(-1,1), (0,1), (1,1), (-1,0), (1,0), (-1,-1), (0,-1), (1,-1)]
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                for offset in offset_list:
                    i_offset = i + offset[0]
                    j_offset = j + offset[1]
                    if i_offset >= 0 and j_offset >= 0 and i_offset < len(self.grid) and j_offset < len(self.grid[i]):
                        self.grid[i][j].addNeighbor(self.grid[i_offset][j_offset])

    def __str__(self):
        output = ""
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j].state:
                    output += '#'
                else:
                    output += '.'
            output += '\n'
        return output

    def alt__str__(self):
        output = ""
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                output += str(self.grid[i][j])
            output += '\n'
        return output
               

class Light:
    def __init__(self, curr_state, neighbor_list):
        self.state = curr_state
        self.neighbor_list = neighbor_list
        self.neighbors_on = 0
        self.is_corner = False

    def update(self):
        if self.is_corner:
            return
        if self.state:
            if self.neighbors_on < 2 or self.neighbors_on > 3:
                self.state = False
        else:
            if self.neighbors_on == 3:
                self.state = True

    def updateNeighborsOn(self):
        self.neighbors_on = 0
        for neighbor in self.neighbor_list:
            if neighbor.state:
                self.neighbors_on += 1

    def addNeighbor(self, neighbor):
        if neighbor.state:
            self.neighbors_on += 1
        self.neighbor_list.append(neighbor)
    
    def __str__(self):
        if self.state:
            return "#" + str(self.neighbors_on)
        else:
            return "." + str(self.neighbors_on)

def main(data):
    grid = Grid(data)
    duration = 100
    for i in range(duration):
        grid.update()
    return grid.countLights()

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))
