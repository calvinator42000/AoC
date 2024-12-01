import sys

class Condition:
    def __init__(self, statement):
        if ':' in statement:
            self.type = 1
            cond, self.result = statement.split(':')
            self.cat = cond[0]
            self.comp = cond[1]
            self.val = int(cond[2:])
        else:
            self.type = 0
            self.cat = None
            self.comp = None
            self.val = None
            self.result = statement


def solve(data):
    workflows = parseData(data.split('\n'))
    accepted = getRanges(workflows)
    total_accepted = 0
    for part_range in accepted:
        range_size = 1
        for key in part_range.keys():
            range_size = range_size * len(part_range[key])
        total_accepted += range_size
    return total_accepted

def getRanges(workflows):
    part_ranges = {'x':range(1,4001),'m':range(1,4001),'a':range(1,4001),'s':range(1,4001)}
    accepted = []
    queue = [(part_ranges, 'in')]
    while len(queue) > 0:
        rng, dest = queue.pop(0)
        if dest == 'A':
            accepted.append(rng)
            continue
        if dest == 'R':
            continue
        for cond in workflows[dest]:
            new_range = {'x':rng['x'],'m':rng['m'],'a':rng['a'],'s':rng['s']}
            if cond.comp == '<':
                if cond.val in rng[cond.cat]:
                    new_range[cond.cat] = range(rng[cond.cat].start, cond.val)
                    rng[cond.cat] = range(cond.val, rng[cond.cat].stop)
                    queue.append((new_range, cond.result))
                elif cond.val >= rng[cond.cat].stop:
                    queue.append((new_range, cond.result))
            elif cond.comp == '>':
                if cond.val in rng[cond.cat]:
                    new_range[cond.cat] = range(cond.val+1, rng[cond.cat].stop)
                    rng[cond.cat] = range(rng[cond.cat].start, cond.val+1)
                    queue.append((new_range, cond.result))
                elif cond.val < rng[cond.cat].start:
                    queue.append((new_range, cond.result))
            else:
                queue.append((new_range, cond.result))
    return accepted

def parseData(data_lines):
    workflows = {}
    collecting_parts = False
    for line in data_lines:
        if len(line) == 0:
            break
        elif not collecting_parts:
            name, flow = line.split('{')
            flow = flow[:-1]
            cond_list = flow.split(',')
            cond_list = list(map(lambda x: Condition(x), cond_list))
            workflows[name] = cond_list
    return workflows


if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
