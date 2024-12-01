import sys

def solve(data):
    game_dict = parseData(data.split('\n'))
    id_sum = 0
    for game_id in game_dict.keys():
        game_content = game_dict[game_id]
        if not (game_content[0] > 12 or game_content[1] > 13 or game_content[2] > 14):
            id_sum += game_id
    return id_sum

def parseData(data_lines):
    game_dict = {}
    for line in data_lines:
        parsed_line = line.split(": ")
        game_id = int(parsed_line[0].split(' ')[1])
        game_content_list = parsed_line[1].split('; ')
        red = 0
        blue = 0
        green = 0
        for content in game_content_list:
            parsed_content = content.split(', ')
            for cube in parsed_content:
                cube_info = cube.split(' ')
                if cube_info[1] == "red":
                    red = max(int(cube_info[0]),red)
                elif cube_info[1] == "green":
                    green = max(int(cube_info[0]),green)
                elif cube_info[1] == "blue":
                    blue = max(int(cube_info[0]),blue)
        game_dict[game_id] = (red,green,blue)
    return game_dict

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
