# how many floors do you visit as an eleva..., I mean, lift
filename = 'input12.txt'
#filename = 'test12.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

floors = []
for l in ls:
    keep_going, n = list(map(int, l.split()))
    floors.append([keep_going, n])

total = 1
up = True
cur_floor = 0
while cur_floor > -1 and cur_floor < len(floors):
    keep_going, n = floors[cur_floor]
    if keep_going != 1:
        up = not up
    if up:
        cur_floor += n
    else:
        cur_floor -= n
    #print("Now at floor", cur_floor)
    total += 1

print(f"We visited {total} floors")
