import sys
import copy

class Graph:
    def __init__(self, route_list):
        self.nodes = {"Start": Node("Start", visited = True)}
        for route in route_list:
            edge = self.processEdge(route)
            if not edge.start in self.nodes:
                self.nodes[edge.start] = Node(edge.start)
                self.nodes["Start"].addEdge(edge.start, 0)
            if not edge.dest in self.nodes:
                self.nodes[edge.dest] = Node(edge.dest)
                self.nodes["Start"].addEdge(edge.dest, 0)
            self.nodes[edge.start].addEdge(edge.dest, edge.dist)
            self.nodes[edge.dest].addEdge(edge.start, edge.dist)

    def generateRoutes(self, location, route_list, route = ["Start"], dist_traveled = 0):
        for edge in self.nodes[location].edge_list.keys():
            if not edge in route:
                new_route = route + [edge]
                new_dist = dist_traveled + self.nodes[location].getDist(edge)
                self.generateRoutes(edge, route_list, new_route, new_dist)
                if len(new_route) == len(self.nodes.keys()):
                    route_list.append((new_dist, new_route))
    
    def getNode(self, location):
        return self.nodes[location]

    def processEdge(self, route):
        parsed_route = route.split(" ")
        ## route = "<start> to <dest> = <dist>"
        edge = Edge(parsed_route[0], parsed_route[2], int(parsed_route[4]))
        return edge

    def __str__(self):
        output = ""
        for n in self.nodes.keys():
            output += str(self.nodes[n]) + '\n'
        return output


class Node:
    def __init__(self, location, visited = False):
        self.location = location
        self.edge_list = {}
        self.visited = visited

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
            output += edge + "-" + str(self.edge_list[edge])
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
    graph.generateRoutes("Start", route_list)
    route_list.sort(reverse = True)
    return route_list[0][0]

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))
