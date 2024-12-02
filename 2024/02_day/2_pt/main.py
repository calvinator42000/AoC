import sys

def is_safe(report):
    diffs = [report[i]-report[i+1] for i in range(len(report)-1)]
    if not (all(i<0 for i in diffs) or all(i>0 for i in diffs)):
        return False
    for i in diffs:
        if i<-3 or i>3:
            return False
    return True

def solve(data):
    line_list = [list(map(int,line.split())) for line in data.split('\n')]
    safe_reports = 0
    for report in line_list:
        if is_safe(report):
            safe_reports += 1
        else:
            for i in range(len(report)):
                dampened_report = report[0:i]+report[i+1:]
                if is_safe(dampened_report):
                    safe_reports += 1
                    break
    return safe_reports

if __name__ == "__main__":
    print(solve(open(sys.argv[1]).read().rstrip()))
