import sys
import re

def main(data):
    num_sum = 0
    num_dict = {'one':'1','1':'1','two':'2','2':'2','three':'3','3':'3','four':'4','4':'4','five':'5','5':'5','six':'6','6':'6','seven':'7','7':'7','eight':'8','8':'8','nine':'9','9':'9','zero':'0','0':'0'}
    for line in data.split('\n'):
        num_sum += int("".join([*map(num_dict.get, [re.findall(r'(?=(\d|' + '|'.join(tuple(num_dict.keys())) + '))', line)[num] for num in (0,-1)])]))
    return num_sum

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))
