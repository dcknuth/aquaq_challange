# kern all the ascii letters and count the total number of spaces
filename = 'input16.txt'
#filename = 'test16.txt'
ascii_file = 'asciialphabet.txt'

# the ascii letters are always 6 rows, but are a variable number of
#  columns. Let's get them into a dictionary for lookup. Let's also use
#  '.' instead of space to match the examples
letters = dict()
with open(ascii_file) as f:
    ls = f.read()
if ls.endswith('\n'):
    ls = ls[:-1]
ls = ls.split('\n')
i = 0
cur_letter = 'A'
while i < len(ls):
    j = 0
    cur_grid = []
    while j < 6:
        cur_grid.append(ls[i+j].replace(' ', '.'))
        j += 1
    letters[cur_letter] = cur_grid[:]
    i += j
    cur_letter = chr(ord(cur_letter) + 1)

def addKerned(s, l):
    '''Take an ascii string and an ascii letter. Add the letter to the
    string fully kerned'''
    # case of the first letter
    if len(s[0]) == 0:
        for i, r in enumerate(s):
            r.extend(l[i][:])
        return()
    # count space distance per row for the new letter
    spaces_per_row = []
    for i, r in enumerate(s):
        back = 0
        while r[back-1] != '#':
            back -= 1
        forward = 0
        while l[i][forward] != '#':
            forward += 1
        spaces_per_row.append(abs(back) + forward)
    kern_by = min(spaces_per_row)
    # add the new letter with correct kerning
    new_letter = [['.'],['.'],['.'],['.'],['.'],['.']]
    for i in range(len(l)):
        new_letter[i].extend(l[i][:])
    for i, r in enumerate(s):
        cur_kern = kern_by
        while cur_kern > 0:
            if new_letter[i][0] == '.':
                new_letter[i].pop(0)
            else:
                r.pop()
            cur_kern -= 1
        r.extend(new_letter[i])

# add on each letter with kerning
with open(filename) as f:
    ls = f.read().strip()
full_str = [[] for x in range(6)]
for l in ls:
    addKerned(full_str, letters[l])

# print final
# for r in full_str:
#     print(''.join(r))

# add up all the spaces ('.'s)
total_spaces = 0
for r in full_str:
    cur_str = ''.join(r)
    total_spaces += cur_str.count('.')
print("Total number of spaces in the combined string is", total_spaces)
