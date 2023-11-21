import sys

class Sue:
    def __init__(self, num, known_props):
        self.num = num
        self.props = {}
        for key in known_props.keys():
            self.props[key] = known_props[key]

    def __str__(self):
        output = "Sue " + self.num + ": "
        first_in = True
        for prop in self.props.keys():
            if first_in:
                output += prop + ": " + str(self.props[prop])
                first_in = False
            else:
                output += ", " + prop + ": " + str(self.props[prop])
        return output


def main(data):
    sue_list = parse_data(data.split('\n'))
    MFCSAM_output = {}
    MFCSAM_output['children'] = 3
    MFCSAM_output['cats'] = 7
    MFCSAM_output['samoyeds'] = 2
    MFCSAM_output['pomeranians'] = 3
    MFCSAM_output['akitas'] = 0
    MFCSAM_output['vizslas'] = 0
    MFCSAM_output['goldfish'] = 5
    MFCSAM_output['trees'] = 3
    MFCSAM_output['cars'] = 2
    MFCSAM_output['perfumes'] = 1
    target_sue = find_sue(MFCSAM_output, sue_list)
    return target_sue.num

def find_sue(test_set, sue_list):
    for sue in sue_list:
        valid_sue = True
        for prop in sue.props.keys():
            if sue.props[prop] != test_set[prop]:
                valid_sue = False
        if valid_sue:
            return sue

def parse_data(data_list):
    sue_list = []
    for line in data_list:
        known_props = {}
        parsed_line = line.split(' ')
        num = parsed_line[1][:len(parsed_line[1])-1]
        i = 2
        while i < len(parsed_line):
            ## Account for last item not ending with a ','
            if parsed_line[i+1][-1] != ',':
                known_props[parsed_line[i][:len(parsed_line[i])-1]] = int(parsed_line[i+1])
            else:
                known_props[parsed_line[i][:len(parsed_line[i])-1]] = int(parsed_line[i+1][:len(parsed_line[i+1])-1])
            i += 2
        sue_list.append(Sue(num, known_props))
    return sue_list


if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))
