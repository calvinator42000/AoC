import sys

def main(data):
    wires = {}
    lines = data.split('\n')
    ## Initialize the wires
    for l in lines:
        parseLine(l, wires)
    while not checkForExpressions(wires):
        for wire in wires.keys():
            if isinstance(wire_list[wire], tuple):
                computeCommand(wires, wire)
    return 0

def computeCommand(wire_list, key):
    wire = wire_list[key]
    command = wire[0]
    args = wire[1]
    signal = 0
    if command == "NOT":
        arg_sig = wire_list[args[0]]
        if isinstance(arg_sig, int)
            
    elif command == "AND":
        pass
    elif command == "OR":
        pass
    elif command == "LSHIFT":
        pass
    elif command == "RSHIFT":
        print("ERROR: Unknown Command - '%s'", command)

def checkForExpressions(wire_list):
    for wire in wire_list.keys():
        if isinstance(wire_list[wire], tuple):
            return False
    return True

def parseLine(line, wire_list):
    ## signal = (command, [params])
    signal = None
    args = line.split(" ")
    if "NOT" in args:
        signal = (args[0], [args[1]])
    elif "AND" in args or \
         "OR" in args or \
         "LSHIFT" in args or \
         "RSHIFT" in args:
        signal = (args[1], [args[0],args[2]])
    else:
        signal = int(args[0])
    wire_list[args[len(args)-1]] = signal
    return

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))
