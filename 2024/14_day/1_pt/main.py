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
    def get_quad(self, grid):
        x_split = grid.w // 2
        y_split = grid.h // 2
        if self.px < x_split and self.py < y_split:
            return 1
        elif self.px > x_split and self.py < y_split:
            return 2
        elif self.px < x_split and self.py > y_split:
            return 3
        elif self.px > x_split and self.py > y_split:
            return 4
        else:
            return 0

def solve(data):
    # grid = Grid(11, 7)
    grid = Grid(101, 103)
    seconds = 100
    quad_count = [0, 0, 0, 0, 0]
    robot_list = []
    for line in data.split('\n'):
        robot = Robot(*map(int,re.findall('-?\d+', line)))
        robot.move(seconds, grid)
        robot_list.append(robot)
        quad_count[robot.get_quad(grid)] += 1
    safety_factor = math.prod(quad_count[1:])
    return safety_factor

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
