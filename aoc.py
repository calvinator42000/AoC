import datetime
import argparse
from importlib import import_module

# Get arguments for the date and part, with the defaults being the current date and Part 1
cur_date = datetime.datetime.now()

parser = argparse.ArgumentParser(prog="Advent of Code Solver")
parser.add_argument("-y", "--year", default=cur_date.year, type=int)
parser.add_argument("-d", "--day", default=cur_date.day, type=int)
parser.add_argument("-p", "--part", default=1, type=int)
parser.add_argument("-t", "--test", nargs='?', const=1, default=0, type=int)

args = parser.parse_args()
year = args.year
day = args.day
part = args.part
test = args.test
input_file = ""
if year < 100:
    year += 2000
if test:
    input_file = "test_input"
    if test > 1:
        input_file += str(test-1)
else:
    input_file = "input"

print("Year:", year)
print("Day:", day)
print("Part:", part)
print("Input_File:", input_file)

input_path = "%d/%02d_day/%01d_pt/%s" % (year, day, part, input_file)
print("Input_Path:", input_path)
package_path = "%d.%02d_day.%01d_pt" % (year, day, part)
print("Package_Path:", package_path)
mod = import_module(".main", package_path)
print()

print("Result:")
result = mod.solve(open(input_path).read().rstrip())
print(result)