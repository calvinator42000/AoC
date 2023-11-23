import sys
from random import shuffle
import copy

def main(data):
    molecule, replacement_list = parseData(data.split('\n'))
    #replacement_list.sort(key = lambda x: len(x[0]), reverse = True)
    generation_list = generateMolecule(molecule, "e", replacement_list, [molecule])
    for generation in generation_list:
        print(generation)
    generation_list.sort(key = lambda x: len(x))
    return len(generation_list[0])-1

def generateMolecule(start, goal, replacement_list, generation, generation_list = [], black_list = []):
    if (start + str(len(generation))) in black_list:
        return generation_list
    if start == goal:
        if not generation in generation_list:
            generation_list.append(generation)
            print("SOLUTION: " + str(len(generation)-1))
        return generation_list
    if 'e' in start:
        return generation_list
    #print("(" + str(len(generation)) + ") Current Target: " + start + " (" + str(len(generation)) + ")")
    for replacement in replacement_list:
        element = replacement[0]
        for i in range(len(start)):
            if i+len(element) <= len(start) and start[i:i+len(element)] == element:
                new_molecule = start[0:i] + replacement[1] + start[i+len(element):]
                if not new_molecule in generation:
                    replacement_list_copy = copy.copy(replacement_list)
                    shuffle(replacement_list_copy)
                    generateMolecule(new_molecule, goal, replacement_list_copy, generation + [new_molecule], generation_list, black_list)
    #print("(" + str(len(generation)) + ") End Branch for: " + start + " (" + str(len(generation)) + ")")
    black_list.append(start + str(len(generation)))
    return generation_list

def getNumElements(molecule):
    num_elements = 0
    i = 0
    while i < len(molecule):
        ## Not accounting for the 'e' element
        if molecule[i].isupper():
            ## Element is in format "Aa"
            if i+1 < len(molecule) and molecule[i+1].islower() and molecule[i+1] != 'e':
                num_elements += 1
                i += 2
            ## Element is in format "a"
            else:
                num_elements += 1
                i += 1
        elif molecule[i] == 'e':
            num_elements += 1
            i += 1
        else:
            print("ERROR: Unrecognized element: " + molecule[i] + " (" + str(i) + ")")
    return num_elements

def parseData(data_list):
    line_index = 0
    replacement_list = []
    while len(data_list[line_index]) > 0:
        parsed_line = data_list[line_index].split(' ')
        replacement_list.append((parsed_line[2], parsed_line[0]))
        line_index += 1
    molecule = data_list[line_index+1]
    return (molecule, replacement_list)

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))
