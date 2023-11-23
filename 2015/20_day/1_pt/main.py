import sys
import math

def main(data):
    required_presents = int(data)
    i = 0
    present_count = 0
    while present_count < int(required_presents/10):
        i += 1
        present_count = factorSum(i)
    return i

def factorSum(number):
    factor_sum = 1
    for i in range(2, int(math.sqrt(number))+1):
        curr_term = 1
        curr_sum = 1
        while number % i == 0:
            curr_term = curr_term * i
            curr_sum += curr_term
            number = int(number / i)
        factor_sum = factor_sum * curr_sum
    if number > 2:
        factor_sum = factor_sum * (number + 1)
    return factor_sum

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))
