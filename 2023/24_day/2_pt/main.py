import sys
import z3

class Ray:
    def __init__(self, start, dir):
        self.x, self.y, self.z = tuple(map(float, start))
        self.a, self.b, self.c = tuple(map(float, dir))

    def getLoc(self, time):
        return (self.x+time*self.a, self.y+time*self.b, self.z+time*self.c)
    
    def __str__(self):
        return f"{int(self.x)}, {int(self.y)}, {int(self.z)} @ {int(self.a)}, {int(self.b)}, {int(self.c)}"

def main(data):
    ray_list = parseData(data.split('\n'))
    return getSolRayZ3(ray_list)

def getSolRayZ3(ray_list):
    x, y, z, a, b, c = map(z3.Real, "xyzabc")
    t = [z3.Real(f"{i}") for i in range(len(ray_list))]
    s = z3.Solver()
    for i in range(len(ray_list)):
        r = ray_list[i]
        s.add(x+t[i]*a == r.x+t[i]*r.a)
        s.add(y+t[i]*b == r.y+t[i]*r.b)
        s.add(z+t[i]*c == r.z+t[i]*r.c)
    s.check()
    m = s.model()
    return m.eval(x+y+z)

## Soluion Works but it took an hour to get to time_limit 40,000 when times would get into the hundreds billions
def getSolRay(ray_list):
    ray_a = ray_list.pop(0)
    ray_b = ray_list.pop(1)
    test_ray = None
    found_ray = False
    a_time = 0
    time_limit = 2
    while not found_ray:
        if time_limit % 500 == 0:
            print(time_limit)
        for t in range(1,time_limit):
            a_pos = ray_a.getLoc(t)
            b_pos = ray_b.getLoc(time_limit)
            test_dir = (a_pos[0]-b_pos[0], a_pos[1]-b_pos[1], a_pos[2]-b_pos[2])
            test_ray = Ray(a_pos, test_dir)
            if validRay(test_ray, ray_list):
                found_ray = True
                a_time = t
                break
            a_pos = ray_a.getLoc(time_limit)
            b_pos = ray_b.getLoc(t)
            test_dir = (a_pos[0]-b_pos[0], a_pos[1]-b_pos[1], a_pos[2]-b_pos[2])
            test_ray = Ray(a_pos, test_dir)
            if validRay(test_ray, ray_list):
                found_ray = True
                a_time = time_limit
                break
        time_limit += 1
    test_ray.x, test_ray.y, test_ray.z = test_ray.getLoc(-a_time)
    return test_ray

def validRay(x, ray_list):
    for ray in ray_list[:2]:
        if not intersects(x,ray):
            return False
    return True

def intersects(i, j):
    ## Solve using Parametric Form
    try:
        s = (i.b*(j.x-i.x)+i.a*(i.y-j.y))/(i.a*j.b-i.b*j.a)
        t = (j.x+j.a*s-i.x)/i.a
    except ZeroDivisionError:
        ## Case when lines are parallel (don't intersect)
        return False
    x = i.x + i.a*t
    y = i.y + i.b*t
    z = i.z + i.c*t
    ## Ensure intersection happens at integer position
    if not x%1.0+y%1.0+z%1.0 == 0:
        return False
    ## Ensure calculation are correct. Will also catch floating point precision errors
    if x != j.x + j.a*s or y != j.y + j.b*s or z != j.z + j.c*s:
        return False
    return True

def parseData(line_list):
    ray_list = []
    for line in line_list:
        characters = tuple(map(int, line.replace(",","").replace(" @ "," ").replace("  "," ").split(' ')))
        ray_list.append(Ray(characters[:3], characters[3:]))
    return ray_list

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))
