import sys

def solve(data):
    wire_list = {}
    command_list = []
    lines = data.split('\n')
    ## Initialize the wires
    for l in lines:
        parseLine(l, wire_list, command_list)
    while len(command_list) > 0:
        completed_cmds = []
        for index in range(len(command_list)):
            result = processCommand(wire_list, command_list[index])
            if result:
                completed_cmds.append(index)
        completed_cmds.sort(reverse=True)
        for cmd_index in completed_cmds:
            command_list.pop(cmd_index)
    return printWires(wire_list)

def processCommand(wire_list, command):
    target = command[0]
    operation = command[1]
    args = command[2]
    signal = None
    for index in range(len(args)):
        ## Check if raw signal value
        try:
            args[index] = int(args[index])
        except ValueError:
            ## Check if wire has raw signal value computed
            try:
                args[index] = int(wire_list[args[index]])
            except TypeError:
                return False
    if operation == "ASSIGN":
        signal = args[0]
    elif operation == "NOT":
        signal = args[0] ^ 0xffff
    elif operation == "AND":
        signal = args[0] & args[1]
    elif operation == "OR":
        signal = args[0] | args[1]
    elif operation == "LSHIFT":
        signal = args[0] << args[1]
    elif operation == "RSHIFT":
        signal = args[0] >> args[1]
    wire_list[target] = signal
    return True

def parseLine(line, wire_list, command_list):
    ## command = (target, command, [params])
    command = None
    args = line.split(" ")
    wire_name = args[len(args)-1]
    if "NOT" in args:
        command = (wire_name, args[0], [args[1]])
    elif "AND" in args or \
         "OR" in args or \
         "LSHIFT" in args or \
         "RSHIFT" in args:
        command = (wire_name, args[1], [args[0], args[2]])
    else:
        command = (wire_name, "ASSIGN", [args[0]])
    wire_list[wire_name] = None 
    command_list.append(command)

def printWires(wire_list):
    output = ""
    keys = list(wire_list.keys())
    keys.sort()
    keys.sort(key=len)
    for wire in keys:
        output += wire + ": " + str(wire_list[wire]) + "\n"
    return output

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
