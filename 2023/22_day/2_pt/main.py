import sys
import numpy
import copy

class Space:
    def __init__(self, bricks):
        self.bricks = bricks
        self.grid = numpy.full(self.getDims(bricks.values()), '.')
        for brick in bricks.values():
            self.updateGrid(brick)
        self.simFall()
        return
    
    def simFall(self):
        while not self.allRested():
            for key in self.bricks.keys():
                can_drop = True
                if self.bricks[key].rested:
                    continue
                new_brick = copy.deepcopy(self.bricks[key])
                new_brick.drop()
                for coord in new_brick.coords:
                    if self.grid[*coord] != '.' and self.grid[*coord] != new_brick.id:
                        can_drop = False
                        break
                if can_drop:
                    self.updateGrid(new_brick)
        for key in self.bricks.keys():
            below_coords = list(map(lambda coord: (coord[0], coord[1], coord[2]-1), self.bricks[key].coords))
            for coord in below_coords:
                below_item = self.grid[*coord]
                if below_item != '.' and below_item != self.bricks[key].id:
                    self.bricks[key].below.add(below_item)
            above_coords = list(map(lambda coord: (coord[0], coord[1], coord[2]+1), self.bricks[key].coords))
            for coord in above_coords:
                above_item = self.grid[*coord]
                if above_item != '.' and above_item != self.bricks[key].id:
                    self.bricks[key].above.add(above_item)
        return
    
    def updateGrid(self, new_brick):
        ## Check that the space isn't occupied
        for coord in new_brick.coords:
            if self.grid[*coord] != '.' and self.grid[*coord] != new_brick.id:
                print(f"ERROR: Brick already exists in {coord}\nOriginal Brick: {self.bricks[self.grid[*coord]]}\nOffending Brick: {new_brick}")
                return
        old_brick = self.bricks[new_brick.id]
        for coord in old_brick.coords:
            self.grid[*coord] = '.'
        for coord in new_brick.coords:
            self.grid[*coord] = new_brick.id
        ## Check if resting
        for coord in new_brick.coords:
            below_space = self.grid[coord[0],coord[1],coord[2]-1]
            if coord[2] == 1 or (below_space != '.' and self.bricks[below_space].rested):
                new_brick.rested = True
        self.bricks[new_brick.id] = new_brick
    
    def allRested(self):
        for brick in self.bricks.values():
            if not brick.rested:
                return False
        return True

    def getChainReaction(self):
        sorted_bricks = sorted(self.bricks.values(), key=lambda x: min(x.z), reverse=True)
        chain_record = {}
        for brick in sorted_bricks:
            print(f"Brick {len(chain_record.keys())} out of {len(self.bricks)}")
            toppled_bricks = set()
            queue = [brick.id]
            chain_record[brick.id] = set()
            while len(queue) > 0:
                next_brick = self.bricks[queue.pop(0)]
                toppled_bricks.add(next_brick.id)
                for above_brick in next_brick.above:
                    if self.bricks[above_brick].below.issubset(toppled_bricks) and not above_brick in toppled_bricks:
                        queue.append(self.bricks[above_brick].id)
            chain_record[brick.id].update(set(toppled_bricks))
            chain_record[brick.id].remove(brick.id)
        return chain_record

    def getDims(self, brick_list):
        x = 0
        y = 0
        z = 0
        for brick in brick_list:
            x = max(x, max(brick.x))
            y = max(y, max(brick.y))
            z = max(z, max(brick.z))
        return (x+1,y+1,z+1)
    
    def __str__(self):
        rows = []
        rows.append(' '*(len(self.grid)//2) + 'x' + ' '*((len(self.grid)//2)+2)+ ' '*(len(self.grid[0])//2) + 'y' + ' '*(len(self.grid[0])//2))
        rows.append("".join(map(str,range(len(self.grid)))) + "  " + "".join(map(str,range(len(self.grid[0])))))
        at_start = True
        for k in range(len(self.grid[0,0])-1,0,-1):
            row = ""
            for i in range(len(self.grid)):
                curr_val = '.'
                for j in range(len(self.grid[0])):
                    if self.grid[i,j,k] != '.':
                        at_start = False
                        if curr_val == '.':
                            curr_val = self.grid[i,j,k]
                        elif curr_val != self.grid[i,j,k]:
                            curr_val = '?'
                            break
                row += curr_val
            row += "  "
            for j in range(len(self.grid[0])):
                curr_val = '.'
                for i in range(len(self.grid)):
                    if self.grid[i,j,k] != '.':
                        at_start = False
                        if curr_val == '.':
                            curr_val = self.grid[i,j,k]
                        elif curr_val != self.grid[i,j,k]:
                            curr_val = '?'
                            break
                row += curr_val
            row += " " + str(k)
            if not at_start:
                rows.append(row)
        rows.append('-'*(len(self.grid)) + "  " + '-'*(len(self.grid)) + " 0")
        rows[-(-(len(rows)-2)//2)+1] += " z"
        return "\n".join(rows)

class Brick:
    def __init__(self, id, end_a, end_b):
        self.id = id
        self.x = [end_a[0], end_b[0]]
        self.y = [end_a[1], end_b[1]]
        self.z = [end_a[2], end_b[2]]
        x,y,z = map(sorted, [self.x,self.y,self.z])
        self.coords = [(i,j,k) for i in range(x[0], x[1]+1) for j in range(y[0], y[1]+1) for k in range(z[0], z[1]+1)]
        self.rested = min(self.z) == 1
        ## Refers to bricks directly on above or below the self (touching)
        self.above = set()
        self.below = set()
    
    def drop(self):
        for i in range(len(self.coords)):
            self.coords[i] = (self.coords[i][0], self.coords[i][1], self.coords[i][2]-1)
    
    def __str__(self):
        return f"id: {self.id}\nloc: {self.x[0]},{self.y[0]},{self.z[0]}~{self.x[1]},{self.y[1]},{self.z[1]}\nrested: {self.rested}\nabove: {self.above}\nbelow: {self.below}\n"

def main(data):
    brick_dict = parseData(data.split('\n'))
    space = Space(brick_dict)
    chain_record = space.getChainReaction()
    chain_sum = 0
    for val in chain_record.values():
        chain_sum += len(val)
    return chain_sum

def parseData(line_list):
    brick_dict = {}
    for i in range(len(line_list)):
        id = chr(i+65)
        brick_dict[id] = Brick(id, *map(lambda x: list(map(int,x.split(','))), line_list[i].split('~')))
    return brick_dict

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))