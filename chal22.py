# convert to roman numerals, then to integers with A=1, B=2, etc
import roman

filename = 'input22.txt'
#filename = 'test22.txt'

with open(filename) as f:
    ls = f.read().strip().split()

total = 0
ord_offset = ord('A') - 1
for l in ls:
    i = int(l)
    r = roman.toRoman(i)
    for c in r:
        total += ord(c) - ord_offset

print("The sum of the arbitrary conversions is", total)
