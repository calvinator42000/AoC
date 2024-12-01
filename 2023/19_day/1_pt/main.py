import sys

class Workflow:
    def __init__(self, conditions):
        self.conditions = conditions
    
    def run(self, part):
        for cond in self.conditions:
            result = cond.test(part)
            if result:
                return result
        return None

class Condition:
    def __init__(self, statement):
        if ':' in statement:
            self.type = 1
            self.cond, self.result = statement.split(':')
        else:
            self.type = 0
            self.cond = None
            self.result = statement

    def test(self, part):
        if self.type == 1:
            cat = self.cond[0]
            comp = self.cond[1]
            val = int(self.cond[2:])
            if comp == '<':
                if part[cat] < val:
                    return self.result
            elif comp == '>':
                if part[cat] > val:
                    return self.result
            else:
                print(f"ERROR: New comparison operator discovered: {comp}")
            return None
        else:
            return self.result


def solve(data):
    workflows, part_list = parseData(data.split('\n'))
    total_rating = 0
    for part in part_list:
        result = "in"
        while result != 'R' and result != 'A':
            result = workflows[result].run(part)
        if result == 'A':
            total_rating += getRating(part)
    return total_rating

def getRating(part):
    rating = 0
    for cat in part.keys():
        rating += part[cat]
    return rating

def parseData(data_lines):
    workflows = {}
    part_list = []
    collecting_parts = False
    for line in data_lines:
        if len(line) == 0:
            collecting_parts = True
        elif not collecting_parts:
            name, flow = line.split('{')
            flow = flow[:-1]
            cond_list = flow.split(',')
            cond_list = list(map(lambda x: Condition(x), cond_list))
            workflows[name] = Workflow(cond_list)
        else:
            part = {}
            cat_list = line[1:-1].split(',')
            for cat in cat_list:
                name, val = cat.split('=')
                part[name] = int(val)
            part_list.append(part)
    return (workflows, part_list)


if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
