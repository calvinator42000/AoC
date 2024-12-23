import sys
import re

a_cost = 3
b_cost = 1

class Machine:
    def __init__(self, button_a, button_b, prize):
        self.ax, self.ay = button_a
        self.bx, self.by = button_b
        self.px, self.py = prize
        self.memo = dict()

def min_coins(posx, posy, cost, machine):
    if posx == machine.px and posy == machine.py:
        return cost
    if posx > machine.px or posy > machine.py:
        return float('inf')
    curr_pos = (posx, posy)
    if curr_pos in machine.memo:
        return machine.memo[curr_pos]
    push_a = min_coins(posx+machine.ax, posy+machine.ay, cost+a_cost, machine)
    push_b = min_coins(posx+machine.bx, posy+machine.by, cost+b_cost, machine)
    machine.memo[curr_pos] = min(push_a, push_b)
    return machine.memo[curr_pos]

def solve(data):
    total_cost = 0
    line_list = data.split('\n')
    for i in range(0,len(line_list),4):
        button_a = list(map(int,re.findall('\d+', line_list[i])))
        button_b = list(map(int,re.findall('\d+', line_list[i+1])))
        prize = list(map(int,re.findall('\d+', line_list[i+2])))
        machine = Machine(button_a, button_b, prize)
        cost = min_coins(0, 0, 0, machine)
        if cost != float('inf'):
            total_cost += cost
    return total_cost

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
