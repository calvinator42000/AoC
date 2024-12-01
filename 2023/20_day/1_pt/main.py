import sys

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

def solve(data):
    module_dict = parseData(data.split('\n'))
    setConj(module_dict)
    push_count = 1000
    complete_record = {0: 0, 1: 0, 2: ""}
    for push in range(push_count):
        record = pushButton(module_dict)
        for key in record.keys():
            complete_record[key] += record[key]
    return complete_record[0] * complete_record[1]

def pushButton(module_dict):
    record = {0: 0, 1: 0, 2: ""}
    queue = [("broadcaster", False, "button")]
    while len(queue) > 0:
        target, sig, src = queue.pop(0)
        record[sig] += 1
        if sig:
            sig_print = "high"
        else:
            sig_print = "low"
        record[2] += f"{src} -{sig_print}-> {target}\n"
        try:
            queue += module_dict[target].run_command(sig, src)
        except KeyError:
            pass
    return record

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
    print(solve(open(sys.argv[1]).read().rstrip()))
