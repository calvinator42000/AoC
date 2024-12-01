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
    step_count = getLoopPath(animal_pos, grid, pipe_dict)
    return int(step_count/2)

def getLoopPath(animal_pos, grid, pipe_dict):
    curr_pos = animal_pos
    curr_pipe = identifyStart(curr_pos, grid, pipe_dict) 
    last_pos = (-1,-1)
    ## First Step
    next_pos = getNextStep(curr_pos, curr_pipe, last_pos, grid, pipe_dict)
    last_pos = curr_pos
    curr_pos = next_pos
    curr_pipe = grid[curr_pos[0]][curr_pos[1]]
    step_count = 1
    while curr_pos != animal_pos:
        next_pos = getNextStep(curr_pos, curr_pipe, last_pos, grid, pipe_dict)
        last_pos = curr_pos
        curr_pos = next_pos
        curr_pipe = grid[curr_pos[0]][curr_pos[1]]
        step_count += 1
    return step_count

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
