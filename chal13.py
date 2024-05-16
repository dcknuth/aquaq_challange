# what is the sum of the counts of the most repeated blocks
import re
from collections import Counter

filename = 'input13.txt'
#filename = 'test13.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

def most_repeated(s, sub_length):
    if sub_length <= 0 or sub_length > len(s):
        raise ValueError("Invalid substring length")
    # generate all substrings of the given length
    subs = set(s[i:i+sub_length] for i in range(len(s) - sub_length + 1))
    max_count = 0
    repeated_str = ''
    # Check consecutive occurrences
    for sub in subs:
        pattern = re.compile(f'({re.escape(sub)})+')
        matches = pattern.finditer(s)
        for match in matches:
            count = match.group().count(sub)
            if count > max_count:
                max_count = count
                repeated_str = sub
    return(repeated_str, max_count)

total_repeats = 0
for string in ls:
    max_repeats = 0
    repeated_str = ''
    for sub_length in range(len(string)//2, 0, -1):
        substring, count = most_repeated(string, sub_length)
        if count > max_repeats:
            max_repeats = count
            repeated_str = substring
    print("The most repeated substring is", repeated_str,
          "which appears", max_repeats, "times")
    total_repeats += max_repeats

print("Total repeats is", total_repeats)
