import sys
from random import shuffle
import copy

def main(data):
    return generateIntelligently(normalize(parseData(data.split('\n'))))

def generateIntelligently(molecule):
    num_replacements = 0
    new_molecule = molecule
    token_list = ["XX","X(X)","X(X,X)","X(X,X,X)"]
    while new_molecule != "XX":
        for token in token_list:
            for i in range(len(new_molecule)-1):
                if new_molecule[i:i+len(token)] == token:
                    new_molecule = new_molecule[:i] + "X" + new_molecule[i+len(token):]
                    num_replacements += 1
    return num_replacements + 1

def normalize(molecule):
    normalized_molecule = ""
    i = 0
    while i < len(molecule):
        if molecule[i].isupper():
            if i+1 < len(molecule) and molecule[i+1].islower() and molecule[i+1] != 'e':
                if molecule[i:i+2] == "Rn":
                    normalized_molecule += "("
                elif molecule[i:i+2] == "Ar":
                    normalized_molecule += ")"
                else:
                    normalized_molecule += "X"
                i += 2
            else:
                if molecule[i] == "Y":
                    normalized_molecule += ","
                else:
                    normalized_molecule += "X"
                i += 1
    return normalized_molecule

def parseData(data_list):
    line_index = 0
    while len(data_list[line_index]) > 0:
        line_index += 1
    molecule = data_list[line_index+1]
    return molecule

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))
