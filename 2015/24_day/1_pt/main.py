import sys

def main(data):
    pkg_list = parseData(data.split('\n'))
    config_list = getConfigurations(pkg_list)
    for config in config_list:
        print(config)
    return 0

def getConfigurations(pkg_list, curr_config = [[],[],[]], config_list = []):
    for i in range(len(pkg_list)):
        for j in range(len(curr_config)):
            new_pkg_list = [] + pkg_list
            new_curr_config = [] + curr_config
            new_curr_config[j].append(new_pkg_list.pop(i))
            if len(new_pkg_list) == 0:
                group_sum = list(map(sum, new_curr_config))
                ## Are the weights equal?
                if group_sum[0] == group_sum[1] and group_sum[0] == group_[1]:
                    config_list.append(new_curr_config)
            else:
                getConfigurations(new_pkg_list, new_curr_config, config_list)
    return config_list

def parseData(data_list):
    pkg_list = []
    for line in data_list:
        pkg_list.append(int(line))
    pkg_list.sort(reverse = True)
    return pkg_list

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))
