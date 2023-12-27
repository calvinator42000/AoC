import sys
from math import lcm

class Module:
    def __init__(self, definition):
        split_def = definition.split(' ')
        ## Type: 0=broadcaster, 1=Flip-Flop, 2=Conjunction
        if split_def[0][0] == '%':
            self.type = 1
            self.name = split_def[0][1:]
            self.state = False
            self.inputs = None
        elif split_def[0][0] == '&':
            self.type = 2
            self.name = split_def[0][1:]
            self.state = None
            self.inputs = {}
        else:
            self.type = 0
            self.name = split_def[0]
            self.state = None
            self.inputs = None
        self.outputs = list(map(lambda x: x.replace(',',''), split_def[2:]))
    
    def run_command(self, sig, src):
        output_commands = []
        if self.type == 0:
            for output in self.outputs:
                output_commands.append((output, sig, self.name))
        elif self.type == 1:
            if sig == False:
                self.state = not self.state
                for output in self.outputs:
                    output_commands.append((output, self.state, self.name))
        elif self.type == 2:
            self.inputs[src] = sig
            for output in self.outputs:
                output_commands.append((output, not all(self.inputs.values()), self.name))
        return output_commands

def main(data):
    module_dict = parseData(data.split('\n'))
    setConj(module_dict)
    goals = {"kr":0,"zs":0,"kf":0,"qk":0}
    found_goals = False
    push_count = 0
    while not found_goals:
        push_count += 1
        pushButton(module_dict, goals, push_count)
        found_goals = all(map(bool, goals.values()))
    for goal, count in goals.items():
        print(f"{goal} {count}")
    found_goal = False

    return lcm(*(goals.values()))

def pushButton(module_dict, goals, push_count):
    queue = [("broadcaster", False, "button")]
    goal_met = False
    while len(queue) > 0:
        target, sig, src = queue.pop(0)
        if target in goals and not sig and not bool(goals[target]):
            goals[target] = push_count
        try:
            queue += module_dict[target].run_command(sig, src)
        except KeyError:
            pass
    return goal_met

def setConj(module_dict):
    for module in module_dict.keys():
        for output in module_dict[module].outputs:
            try:
                if module_dict[output].inputs != None:
                    module_dict[output].inputs[module] = False
            except KeyError:
                pass
    return None

def parseData(line_list):
    module_dict = {}
    for line in line_list:
        new_module = Module(line)
        module_dict[new_module.name] = new_module
    return module_dict

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))
