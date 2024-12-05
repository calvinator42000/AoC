import sys
import functools

class Page:
    def __init__(self):
        self.before = set()
        self.after = set()

rules = dict()

def parse_data(line_list):
    updates = []
    parsing_rules = True
    for line in line_list:
        if line:
            if parsing_rules:
                a,b = map(int, line.split('|'))
                if not a in rules:
                    rules[a] = Page()
                rules[a].after.add(b)
                if not b in rules:
                    rules[b] = Page()
                rules[b].before.add(a)
            else:
                updates.append(list(map(int, line.split(','))))
        else:
            parsing_rules = False
    return updates

def is_correct_order(update):
    for i in range(len(update)):
        before = set(update[:i])
        after = set(update[i+1:])
        page = update[i]
        if before.intersection(rules[page].after) or after.intersection(rules[page].before):
            return False
    return True

def cmp_func(a, b):
    if b in rules[a].after:
        return -1
    elif b in rules[a].before:
        return 1
    else:
        return 0

def solve(data):
    line_list = data.split('\n')
    updates = parse_data(line_list)
    total = 0
    for update in updates:
        if not is_correct_order(update):
            update.sort(key=functools.cmp_to_key(cmp_func))
            middle_page = update[len(update)//2]
            total += middle_page
    return total

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
