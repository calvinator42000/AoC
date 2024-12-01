import sys

def solve(data):
    pipe_dict = {
            '|': [(-1,0),(1,0)],
            '-': [(0,-1),(0,1)],
            'L': [(-1,0),(0,1)],
            'J': [(-1,0),(0,-1)],
            '7': [(0,-1),(1,0)],
            'F': [(0,1),(1,0)]}
    animal_pos, grid = parseData(data.split('\n'))
    path = getLoopPath(animal_pos, grid, pipe_dict)
    grid[animal_pos[0]][animal_pos[1]] = identifyStart(animal_pos, grid, pipe_dict)
    return countInLoop(path, grid)

def countInLoop(path, grid):
    in_loop_list = []
    in_loop_count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if not (row, col) in path:
                last_turn = None
                edges_past = 0
                above_row = row-1
                for above_row in range(row-1,-1,-1):
                    if (above_row, col) in path:
                        pipe = grid[above_row][col]
                        if pipe == '-':
                            edges_past += 1
                        elif pipe == 'L' or pipe == 'J':
                            last_turn = pipe
                        elif pipe == 'F':
                            if last_turn == 'J':
                                edges_past += 1
                                last_turn = None
                            elif last_turn == 'L':
                                last_turn = None
                            elif last_turn == None:
                                print(f"ERROR: Unexpected pipe at ({above_row},{col})")
                                return None
                        elif pipe == '7':
                            if last_turn == 'L':
                                edges_past += 1
                                last_turn = None
                            elif last_turn == 'J':
                                last_turn = None
                            elif last_turn == None:
                                print(f"ERROR: Unexpected pipe at ({above_row},{col})")
                                return None
                if edges_past % 2 == 1:
                    in_loop_list.append((row,col))
                    in_loop_count += 1
    return in_loop_count

def getLoopPath(animal_pos, grid, pipe_dict):
    curr_pos = animal_pos
    curr_pipe = identifyStart(curr_pos, grid, pipe_dict) 
    last_pos = (-1,-1)
    path = [curr_pos]
    ## First Step
    next_pos = getNextStep(curr_pos, curr_pipe, last_pos, grid, pipe_dict)
    last_pos = curr_pos
    curr_pos = next_pos
    curr_pipe = grid[curr_pos[0]][curr_pos[1]]
    path.append(curr_pos)
    while curr_pos != animal_pos:
        next_pos = getNextStep(curr_pos, curr_pipe, last_pos, grid, pipe_dict)
        last_pos = curr_pos
        curr_pos = next_pos
        curr_pipe = grid[curr_pos[0]][curr_pos[1]]
        path.append(curr_pos)
    return path

def getNextStep(curr_pos, curr_pipe, last_pos, grid, pipe_dict):
    next_pos_cand_list = list(map(lambda x: (x[0]+curr_pos[0],x[1]+curr_pos[1]), pipe_dict[curr_pipe]))
    for next_pos_cand in next_pos_cand_list:
        if next_pos_cand != last_pos:
            return next_pos_cand
    print(f"ERROR: No valid path found:\ncurr_pos: {curr_pos}\ncurr_pipe: {curr_pipe}\nnext_pos_cand_list: {next_pos_cand_list}")
    return None

def identifyStart(curr_pos, grid, pipe_dict):
    pipe_dict_items = pipe_dict.items()
    pipe_list = []
    try:
        ## North
        valid_list = ['|','7','F']
        pipe_cand = grid[curr_pos[0]-1][curr_pos[1]]
        if pipe_cand in valid_list:
            pipe_list.append((-1,0))
    except IndexError:
        pass
    try:
        ## East
        valid_list = ['-','J','7']
        pipe_cand = grid[curr_pos[0]][curr_pos[1]+1]
        if pipe_cand in valid_list:
            pipe_list.append((0,1))
    except IndexError:
        pass
    try:
        ## South
        valid_list = ['|','L','J']
        pipe_cand = grid[curr_pos[0]+1][curr_pos[1]]
        if pipe_cand in valid_list:
            pipe_list.append((1,0))
    except IndexError:
        pass
    try:
        ## West
        valid_list = ['-','L','F']
        pipe_cand = grid[curr_pos[0]][curr_pos[1]-1]
        if pipe_cand in valid_list:
            pipe_list.append((0,-1))
    except IndexError:
        pass
    if len(pipe_list) != 2:
        print(f"ERROR: {pipe_list} is not a valid pipe definition\ncurr_pos: {curr_pos}")
        return None
    for pipe_def in pipe_dict_items:
        inv_pipe_list = [pipe_list[1],pipe_list[0]]
        if pipe_list == pipe_def[1]:
            return pipe_def[0]
        elif inv_pipe_list == pipe_def[1]:
            return pipe_def[0]
    print(f"ERROR: {pipe_list} is not a valid pipe definition")
    return None

def parseData(line_list):
    animal_pos = None
    grid = []
    for line_index in range(len(line_list)):
        grid.append(list(line_list[line_index]))
        if 'S' in line_list[line_index]:
            animal_pos = (line_index, line_list[line_index].index('S'))
    return (animal_pos, grid)

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
