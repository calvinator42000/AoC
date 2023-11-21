import sys

class Reindeer:
    def __init__(self, name, speed, speed_dir, rest_dir):
        self.name = name
        self.speed = speed
        self.fly_dir = speed_dir
        self.rest_dir = rest_dir
        self.fly_timer = 0
        self.rest_timer = 0
        self.distance = 0
        self.flying = True

    def runFrame(self):
        if self.flying:
            self.fly_timer += 1
            self.distance += self.speed
            if self.fly_timer == self.fly_dir:
                self.flying = False
                self.fly_timer = 0
        else:
            self.rest_timer += 1
            if self.rest_timer == self.rest_dir:
                self.flying = True
                self.rest_timer = 0
    
    def __str__(self):
        return self.name + ": " + str(self.distance)

def main(data):
    reindeer_list = makeReindeer(data.split('\n'))
    duration = 2503
    for i in range(duration):
        for deer in reindeer_list:
            deer.runFrame()
    reindeer_list.sort(key=lambda x: x.distance, reverse = True)
    winning_deer = reindeer_list[0]
    return winning_deer.distance

def makeReindeer(data_list):
    reindeer_list = []
    for line in data_list:
        parsed_line = line.split(" ")
        name = parsed_line[0]
        speed = int(parsed_line[3])
        speed_dir = int(parsed_line[6])
        rest_dir = int(parsed_line[13])
        reindeer_list.append(Reindeer(name, speed, speed_dir, rest_dir))
    return reindeer_list

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))
