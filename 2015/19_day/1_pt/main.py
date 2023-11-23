import sys

def main(data):
    molecule, replacement_dict = parseData(data.split('\n'))
    new_molecule_list = []
    i = 0
    while i < len(molecule):
        element = None
        ## Not accounting for the 'e' element
        if molecule[i].isupper():
            ## Element is in format "Aa"
            if i+1 < len(molecule) and molecule[i+1].islower():
                element = molecule[i:i+2]
            ## Element is in format "a"
            else:
                element = molecule[i]
        else:
            print("ERROR: Element begins with lowercase letter: %s at %s", molecule[i], str(i))
            return None
        
        if element in replacement_dict.keys():
            curr_replacement_list = replacement_dict[element]
            for replacement in curr_replacement_list:
                new_molecule = molecule[0:i] + replacement + molecule[i+len(element):]
                if not new_molecule in new_molecule_list:
                    new_molecule_list.append(new_molecule)
        i += len(element)
    return len(new_molecule_list)

def parseData(data_list):
    line_index = 0
    replacement_dict = {}
    while len(data_list[line_index]) > 0:
        parsed_line = data_list[line_index].split(' ')
        if not parsed_line[0] in replacement_dict.keys():
            replacement_dict[parsed_line[0]] = []
        replacement_dict[parsed_line[0]].append(parsed_line[2])
        line_index += 1
    molecule = data_list[line_index+1]
    return (molecule, replacement_dict)

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))
