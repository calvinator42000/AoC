import sys
import re
import math

class Grid:
    def __init__(self, width, height):
        self.w = width
        self.h = height

class Robot:
    def __init__(self, posx, posy, velx, vely):
        self.px, self.py = posx, posy
        self.vx, self.vy = velx, vely
    def move(self, seconds, grid):
        self.px = (self.vx * seconds + self.px) % grid.w
        self.py = (self.vy * seconds + self.py) % grid.h

def solve(data):
    # grid = Grid(11, 7)
    grid = Grid(101, 103)
    robot_list = []
    for line in data.split('\n'):
        robot = Robot(*map(int,re.findall('-?\d+', line)))
        robot_list.append(robot)
    seconds = 39
    # Witnessed two patterns of alignment, found that these occured at
    # geometrically changing intervals. Pattern started at 39 seconds.
    steps = [60,41]
    switch = False
    for robot in robot_list:
        robot.move(39, grid)
    print_grid(grid, robot_list)
    while not input():
        for robot in robot_list:
            robot.move(steps[switch], grid)
        seconds += steps[switch]
        if switch:
            steps[switch] -= 2
        else:
            steps[switch] += 2
        switch = not switch
        print_grid(grid, robot_list)
        print(seconds)
    # Solution: 7412
    return seconds

def print_grid(grid, robot_list):
    output = ""
    for i in range(grid.h):
        for j in range(grid.w):
            robot_count = 0
            for robot in robot_list:
                if robot.px == j and robot.py == i:
                    robot_count += 1
            if robot_count:
                output += str(robot_count)
            else:
                output += '.'
        output += '\n'
    print(output)

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
