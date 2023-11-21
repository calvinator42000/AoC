import sys

class Container:
    def __init__(self, capacity):
        self.capacity = capacity
        self.filled = False

    def __str__(self):
        return str(self.capacity) + ": " + str(self.filled)
        

def main(data):
    containers = []
    for line in data.split('\n'):
        containers.append(Container(int(line)))
    combination_list = generateCombinationList(containers, 150)
    return len(combination_list)

def generateCombinationList(container_list, quantity):
    combination_list = []
    generateCombination(quantity, container_list, combination_list)
    return combination_list

def generateCombination(quantity, container_list, combination_list, next_container_index = 0):
    if quantity == 0:
        combination_list.append(getUsedContainers(container_list))
        return
    if quantity < 0 or next_container_index == len(container_list):
        return
    curr_container = container_list[next_container_index]
    curr_container.filled = False
    generateCombination(quantity, container_list, combination_list, next_container_index+
1)
    if curr_container.capacity <= quantity:
        curr_container.filled = True
        generateCombination(quantity-curr_container.capacity, container_list, combination_list, next_container_index+1)
    curr_container.filled = False

def getUsedContainers(container_list):
    output = ""
    firstTime = True
    for container in container_list:
        if container.filled:
            if firstTime:
                output += str(container.capacity)
                firstTime = False
            else:
                output += ", " + str(container.capacity)
    return output

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))
