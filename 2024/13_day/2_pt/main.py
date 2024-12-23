import sys
import re
import sympy

a_cost = 3
b_cost = 1

class Machine:
    def __init__(self, button_a, button_b, prize):
        self.ax, self.ay = button_a
        self.bx, self.by = button_b
        self.px, self.py = prize
        self.px += 10000000000000
        self.py += 10000000000000
        self.memo = dict()

# I'm so mad it took me this long to figure it out. Eureka moment came shortly 
# after I had to come to terms with the fact that looping through over 10 
# trillion iterations is, in fact, not very realistic.

def min_coins(machine):
    a,b = sympy.symbols('a,b')
    fx = sympy.Eq(machine.ax*a + machine.bx*b, machine.px)
    fy = sympy.Eq(machine.ay*a + machine.by*b, machine.py)
    result = sympy.solve([fx,fy], (a,b))
    if (type(result[a]) == sympy.core.numbers.Integer) and (type(result[b]) == sympy.core.numbers.Integer):
        return result[a]*a_cost + result[b]*b_cost
    return 0

def solve(data):
    total_cost = 0
    line_list = data.split('\n')
    for i in range(0,len(line_list),4):
        button_a = list(map(int,re.findall('\d+', line_list[i])))
        button_b = list(map(int,re.findall('\d+', line_list[i+1])))
        prize = list(map(int,re.findall('\d+', line_list[i+2])))
        machine = Machine(button_a, button_b, prize)
        cost = min_coins(machine)
        if cost != float('inf'):
            total_cost += cost
    return total_cost

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
