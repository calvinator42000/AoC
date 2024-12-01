import sys

def solve(data):
    sequence_list = parseData(data.split('\n'))
    final_sum = 0
    for sequence in sequence_list:
        final_sum += generateHistory(sequence)
    return final_sum

def generateHistory(sequence):
    if sum(sequence) == 0:
        return 0
    new_history = []
    for i in range(1,len(sequence)):
        new_history.append(sequence[i] - sequence[i-1])
    return generateHistory(new_history) + sequence[-1]

def parseData(line_list):
    sequence_list = []
    for line in line_list:
        sequence_list.append(list(map(int,line.split(' '))))
    return sequence_list

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
