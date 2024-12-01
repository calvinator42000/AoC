import sys

def solve(data):
    scores = {}
    for card in data.split('\n'):
        num_win_card = 0
        card_id, card_data = card.split(": ")
        card_id = int(card_id.split(' ')[-1])
        win_num_list, num_list = tuple(map(lambda x: list(map(int, x.lstrip().replace("  ", ' ').split(' '))), card_data.split(" | ")))
        for win_num in win_num_list:
            if win_num in num_list:
                num_win_card += 1
        scores[card_id] = num_win_card
    queue = list(scores.keys())
    for card in queue:
        for i in range(1,scores[card]+1):
            queue.append(card + i)
    return len(queue)

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
