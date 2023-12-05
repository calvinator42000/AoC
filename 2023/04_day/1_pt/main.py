import sys

def main(data):
    points = 0
    for card in data.split('\n'):
        num_win_card = 0
        win_num_list, num_list = tuple(map(lambda x: list(map(int, x.lstrip().replace("  ", ' ').split(' '))), card.split(": ")[1].split(" | ")))
        for win_num in win_num_list:
            if win_num in num_list:
                num_win_card += 1
        points += int(2 ** (num_win_card-1))
    return points

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))
