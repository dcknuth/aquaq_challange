# remove bad data

filename = 'input02.txt'
#filename = 'test02.txt'

with open(filename) as f:
    ls = f.read().strip().split()

# remove bad data
i = 0
while i < len(ls) - 1:
    if ls[i] in ls[i+1:]:
        last = len(ls) - 1 - ls[::-1].index(ls[i])
        new_ls = ls[:i]
        new_ls.extend(ls[last:])
        ls = new_ls
    i += 1

# sum up
total = sum([int(x) for x in ls])

print("Sum of remaining values is", total)
