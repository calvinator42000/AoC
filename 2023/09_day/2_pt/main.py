import sys

def main(data):
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
    return sequence[0] - generateHistory(new_history)

def parseData(line_list):
    sequence_list = []
    for line in line_list:
        sequence_list.append(list(map(int,line.split(' '))))
    return sequence_list

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))
