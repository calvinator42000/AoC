import sys

def main(data):
    strings = data.split('\n')
    nice_count = 0
    for s in strings:
        if check_str(s):
            nice_count = nice_count + 1
    return nice_count

def check_str(string):
    return check_vowels(string) and \
            check_doubles(string) and \
            check_forbidden(string)

def check_vowels(string):
    vowels = "aeiou"
    vowel_count = 0
    for char in string:
        if char in vowels:
            vowel_count = vowel_count + 1
            if vowel_count == 3:
                return True
    return False

def check_doubles(string):
    prev_char = ''
    for char in string:
        if char == prev_char:
            return True
        prev_char = char
    return False

def check_forbidden(string):
    bad_strings = ["ab","cd","pq","xy"]
    for i in range(1,len(string)):
        if string[i-1:i+1] in bad_strings:
            return False
    return True


if __name__ == "__main__":
    print(main(open(sys.argv[1]).read()))
