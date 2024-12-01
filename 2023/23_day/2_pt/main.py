import sys

def solve(data):
    grid = parseData(data.split('\n'))
    start = (0,1)
    end = (len(grid)-1,len(grid[0])-2)
    graph = getGraph(start, end, grid)
    max_dist = dfs(start, end, graph)
    return max_dist

def getVerticies(grid):
    verticies = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != "#" and len(getNeighbors((i,j),grid)) > 2:
                verticies.append((i,j))
    return verticies

def getGraph(start, end, grid):
    graph = {}
    verticies = getVerticies(grid)
    verticies.append(start)
    verticies.append(end)
    for vertex in verticies:
        queue = [vertex]
        visited = [vertex]
        dist = 0
        while len(queue) > 0:
            new_queue = []
            dist += 1
            for node in queue:
                for neighbor in getNeighbors(node, grid):
                    if neighbor not in visited:
                        if neighbor in verticies:
                            if vertex not in graph:
                                graph[vertex] = []
                            graph[vertex].append((neighbor, dist))
                        else:
                            new_queue.append(neighbor)
                        visited.append(neighbor)
            queue = new_queue
    return graph

def dfs(start, end, graph):
    max_dist = 0
    stack = [(start, [], 0)]
    while len(stack) > 0:
        current, curr_path, curr_dist = stack.pop()
        if current == end:
            if curr_dist > max_dist:
                max_dist = curr_dist
        for neighbor in graph[current]:
            if neighbor[0] not in curr_path:
                stack.append((neighbor[0], curr_path + [neighbor[0]], curr_dist + neighbor[1]))
    return max_dist

def getNeighbors(node, grid):
    dir_list = [(-1,0),(0,1),(1,0),(0,-1)]
    neighbors = []
    for dir in dir_list:
        next_node = (node[0]+dir[0], node[1]+dir[1])
        if 0 <= next_node[0] < len(grid) and 0 <= next_node[1] < len(grid[0]) and grid[next_node[0]][next_node[1]] != '#':
            neighbors.append(next_node)
    return neighbors

def parseData(line_list):
    grid = []
    for line in line_list:
        grid.append(list(line))
    return grid

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
