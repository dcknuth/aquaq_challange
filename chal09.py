# multiply your input

filename = 'input09.txt'
#filename = 'test09.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

numbers = list(map(int, ls))
total = 1
for n in numbers:
    total *= n

print("Final number is", total)
# Python makes this easy
