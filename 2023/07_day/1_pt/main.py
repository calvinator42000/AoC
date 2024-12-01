import sys
import re

def solve(data):
    face_list = ('2','3','4','5','6','7','8','9','T','J','Q','K','A')
    hand_list = list(map(lambda x: (x[:5], int(x[6:])), data.split('\n')))
    hand_list_scored = sorted(list(map(lambda x: (x[0], getScore(x[0], face_list), x[1]), hand_list)), key=lambda x: x[1])
    hand_list_scored_grouped = groupByScore(hand_list_scored)
    hand_list_scored_grouped_sorted = []
    for group in hand_list_scored_grouped:
        hand_list_scored_grouped_sorted.append(rankByGroup(group, face_list))
    ranked_hands = []
    for group in hand_list_scored_grouped_sorted:
        for hand in group:
            ranked_hands.append(hand)
    final_score = 0
    for rank in range(1, len(ranked_hands)+1):
        final_score += rank * ranked_hands[rank-1][2]
    return final_score

def getScore(hand, face_list):
    sorted_hand = "".join(sorted(list(hand), key=lambda x: face_list.index(x)))
    regex_list = [r'(.)\1{4}', r'(.)\1{3}', r'(.)\1{1}(.)\2{2}|(.)\3{2}(.)\4{1}', r'(.)\1{2}', r'.?(.)\1.?(.)\2.?', r'(.)\1', r'.*']
    return 7 - (list(map(lambda x: re.search(x, sorted_hand) != None, regex_list)).index(True))

def groupByScore(hand_list_scored):
    score_group_list = []
    curr_score = hand_list_scored[0][1]
    curr_group = [hand_list_scored[0]]
    for i in range(1, len(hand_list_scored)):
        if hand_list_scored[i][1] != curr_score:
            score_group_list.append(curr_group)
            curr_group = []
            curr_score = hand_list_scored[i][1]
        curr_group.append(hand_list_scored[i])
    score_group_list.append(curr_group)
    return score_group_list

def rankByGroup(hand_group, face_list):
    for i in range(4,-1,-1):
        hand_group.sort(key=lambda x: convertHand(x, face_list)[0][i])
    return hand_group

def convertHand(hand, face_list):
    return (list(map(lambda x: face_list.index(x), list(hand[0]))), hand[1], hand[2])

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
