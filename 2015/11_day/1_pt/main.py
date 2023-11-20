import sys

alpha = 'abcdefghijklmnopqrstuvwxyz'
new_alpha = 'abcdefghjkmnpqrstuvwxyz'

def main(data):
    password = fixInitial(data)
    if password == data:
        password = incPass(password)
    while not (checkStraight(password) and checkDoubleDoubles(password)):
        print(password)
        password = incPass(password)
    return password

## Get rid of any initial 'i's, 'l's, and 'o's
def fixInitial(password):
    new_pass = list(password)
    found_bad_char = False
    for i in range(len(password)):
        if found_bad_char:
            new_pass[i] = 'a'
        elif not new_pass[i] in new_alpha:
            new_pass[i] = alpha[(alpha.index(new_pass[i])+1)]
            found_bad_char = True
    return "".join(new_pass)
            

def checkStraight(password):
    straight_count = 1
    last_char = password[0]
    for i in range(1, len(password)):
        if alpha.index(password[i]) == alpha.index(last_char)+1:
            straight_count += 1
            if straight_count == 3:
                return True
        else:
            straight_count = 1
        last_char = password[i]
    return False

def checkDoubleDoubles(password):
    ## If double exists, split string in have by the double
    split_password = splitByDouble(password)
    if not split_password == None:
        ## Look for double in both halves and return true if one half has one
        pass_half_1 = not splitByDouble(split_password[0]) == None
        pass_half_2 = not splitByDouble(split_password[1]) == None
        if pass_half_1 or pass_half_2:
            return True
    return False

def splitByDouble(password):
    if len(password) == 0:
        return None
    last_char = password[0]
    for i in range(1, len(password)):
        if password[i] == last_char:
            return (password[0:i-1], password[i+1:])
        else:
            last_char = password[i]
    return None

def incPass(password):
    next_pass = list(password)
    carry_over = True
    pass_index = len(password)-1
    while carry_over:
        if next_pass[pass_index] == 'z':
            pass_index -= 1
        else:
            while pass_index < len(password):
                next_pass[pass_index] = new_alpha[(new_alpha.index(next_pass[pass_index])+1) % 23]
                pass_index += 1
            carry_over = False
    return "".join(next_pass)

if __name__ == "__main__":
    print(main(open(sys.argv[1]).read().rstrip()))
