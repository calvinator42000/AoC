import sys
import copy

class Graph:
    def __init__(self, route_list):
        self.nodes = {}
        for route in route_list:
            edge = self.processEdge(route)
            if not edge.start in self.nodes:
                self.nodes[edge.start] = Node(edge.start)
            self.nodes[edge.start].addEdge(edge.dest, edge.dist)
        self.syncEdges()

    def generateRoutes(self, location, route_list, route, dist_traveled = 0):
        for edge in self.nodes[location].edge_list.keys():
            if not edge in route:
                new_route = route + [edge]
                new_dist = dist_traveled + self.nodes[location].getDist(edge)
                self.generateRoutes(edge, route_list, new_route, new_dist)
                if len(new_route) == len(self.nodes.keys()):
                    ## Return to start of the route
                    new_route += [new_route[0]]
                    new_dist += self.nodes[new_route[0]].getDist(new_route[len(self.nodes.keys())-1])
                    route_list.append((new_dist, new_route))
    
    def getNode(self, location):
        return self.nodes[location]

    def processEdge(self, route):
        parsed_route = route.split(" ")
        ## route = "<start> would <gain=pos, lose=neg> <dist> happiness unites by sitting next to <dest>."
        dist = int(parsed_route[3])
        if parsed_route[2] == "lose":
            dist = dist * (-1)
        edge = Edge(parsed_route[0], parsed_route[10][:len(parsed_route[10])-1], dist)
        return edge

    def syncEdges(self):
        i = 0
        for i in range(len(self.nodes.keys())):
            start = list(self.nodes.keys())[i]
            for j in range(i+1, len(self.nodes.keys())):
                dest = list(self.nodes.keys())[j]
                a = self.nodes[start]
                b = self.nodes[dest]
                new_dist = a.getDist(dest) + b.getDist(start)
                self.nodes[start].addEdge(dest, new_dist)
                self.nodes[dest].addEdge(start, new_dist)

    def __str__(self):
        output = ""
        for n in self.nodes.keys():
            output += str(self.nodes[n]) + '\n'
        return output


class Node:
    def __init__(self, location, visited = False):
        self.location = location
        self.edge_list = {}

    def addEdge(self, dest, dist):
        self.edge_list[dest] = dist

    def getDist(self, dest):
        return self.edge_list[dest]

    def __str__(self):
        output = self.location + ": "
        first_print = True
        for edge in self.edge_list.keys():
            if not first_print:
                output += ", "
            output += edge + "(" + str(self.edge_list[edge]) + ")"
            first_print = False
        return output


class Edge:
    def __init__(self, start, dest, dist):
        self.start = start
        self.dest = dest
        self.dist = dist


def main(data):
    route_list = data.split("\n")
    graph = Graph(route_list)
    route_list = []
    graph.generateRoutes("Alice", route_list, ["Alice"])
    route_list.sort(reverse = True)
    return route_list[0][0]

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))
