import sys
import re

def solve(data):
    hand_list = list(map(lambda x: (x[:5], int(x[6:])), data.split('\n')))
    hand_list_scored = sorted(list(map(lambda x: (getScore(x[0]), x[1]), hand_list)), key=lambda x: x[0])
    final_score = 0
    for rank in range(1, len(hand_list_scored)+1):
        final_score += rank * hand_list_scored[rank-1][1]
    return final_score

def getScore(hand):
    face_list = ('2','3','4','5','6','7','8','9','T','J','Q','K','A')
    score = getType(hand, face_list) * 100**5
    for card_index in range(5):
        card_score = face_list.index(hand[card_index])
        score += face_list.index(hand[card_index]) * (100**(4-card_index))
    return score

def getType(hand, face_list):
    sorted_hand = "".join(sorted(list(hand), key=lambda x: face_list.index(x)))
    regex_list = [r'(.)\1{4}', r'(.)\1{3}', r'(.)\1{1}(.)\2{2}|(.)\3{2}(.)\4{1}', r'(.)\1{2}', r'.?(.)\1.?(.)\2.?', r'(.)\1', r'.*']
    return 7 - (list(map(lambda x: re.search(x, sorted_hand) != None, regex_list)).index(True))

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
