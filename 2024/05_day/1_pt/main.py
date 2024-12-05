import sys

class Page:
    def __init__(self):
        self.before = set()
        self.after = set()

def parse_data(line_list):
    rules = dict()
    updates = []
    parsing_rules = True
    for line in line_list:
        if line:
            if parsing_rules:
                a,b = map(int, line.split('|'))
                if a in rules:
                    rules[a].after.add(b)
                else:
                    rules[a] = Page()
                    rules[a].after.add(b)
                if b in rules:
                    rules[b].before.add(a)
                else:
                    rules[b] = Page()
                    rules[b].before.add(a)
            else:
                updates.append(list(map(int, line.split(','))))
        else:
            parsing_rules = False
    return rules, updates

def is_correct_order(rules, update):
    for i in range(len(update)):
        before = set(update[:i])
        after = set(update[i+1:])
        page = update[i]
        if before.intersection(rules[page].after) or after.intersection(rules[page].before):
            return False
    return True


def solve(data):
    line_list = data.split('\n')
    rules, updates = parse_data(line_list)
    total = 0
    for update in updates:
        if is_correct_order(rules, update):
            middle_page = update[len(update)//2]
            total += middle_page
    return total

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
