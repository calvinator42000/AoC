import sys

def main(data):
    hailstones = parseData(data.split('\n'))
    area = (200000000000000,400000000000000)
    future_collisions = 0
    for i in range(len(hailstones)):
        a = hailstones[i]
        for j in range(i+1, len(hailstones)):
            b = hailstones[j]
            try:
                x = (a[3]-b[3])/(b[2]-a[2])
            except ZeroDivisionError:
                continue
            y = a[2]*x + a[3]
            if area[0] <= x <= area[1] and area[0] <= y <= area[1]:
                if (x-a[0][0])*a[1][0] >= 0 and (x-b[0][0])*b[1][0] >= 0:
                    future_collisions += 1
    return future_collisions

def parseData(line_list):
    hailstones = []
    for line in line_list:
        characters = tuple(map(int, line.replace(",","").replace(" @ "," ").replace("  "," ").split(' ')))
        pos, vel = (characters[:3], characters[3:])
        slope = vel[1]/vel[0]
        const = (slope*-pos[0]) + pos[1]
        hailstones.append((pos, vel, slope, float(const)))
    return hailstones

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))
