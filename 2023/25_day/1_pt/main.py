import sys
import networkx as nx

## Using Stoer-Wagner Algorithm

def solve(data):
    conn_list = parseData(data.split('\n'))
    graph = nx.Graph(conn_list)
    subgraphs = nx.stoer_wagner(graph)[1]
    return len(subgraphs[0]) * len(subgraphs[1])

def parseData(line_list):
    conn_list = []
    for line in line_list:
        left, right = line.split(": ")
        for comp in right.split(' '):
            conn_list.append((left, comp))
    return conn_list

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
