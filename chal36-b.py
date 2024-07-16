# solve the math puzzles (tetonors) and sum up the answers
from collections import defaultdict
filename = 'input36.txt'
filename = 'test36.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

def solve(g, i):
    all_pairs = defaultdict(set)
    answer_set = []
    g_left = list(g)
    i_left = list(i)
    g_needed = defaultdict(int)
    # count up the number of each number in g
    for num in g:
        g_needed[num] += 1
    # make combo lists for x+y, x*y and both
    for a, x in enumerate(i):
        for y in i[a+1:]:
            if x + y in g and x * y in g:
                all_pairs[x+y].add((x, y))
                all_pairs[x*y].add((x, y))
    while len(g_left) > 0:
        # remove numbers that only have the number they need and their pair
        to_remove = []
        for num in all_pairs.keys():
            if len(all_pairs[num]) == g_needed[num]:
                x, y = next(iter(all_pairs[num]))
                answer_set.append((x, y))
                if x + y == num:
                    to_remove.append([num, 's', x, y])
                    to_remove.append([x * y, 'p', x, y])
                else:
                    to_remove.append([num, 'p', x, y])
                    to_remove.append([x + y, 's', x, y])
                i_left.remove(x)
                i_left.remove(y)
                break
        for cur in to_remove:
            g_needed[cur[0]] -= 1
            g_left.remove(cur[0])
            all_pairs[cur[0]].discard((cur[2], cur[3]))
            if len(all_pairs[cur[0]]) == 0:
                del all_pairs[cur[0]]
    return(answer_set)


# loop through puzzles and sum up
total = 0
while len(ls) > 0:
    _, g = ls.pop(0).split(':')
    g = tuple(map(int, g.split()))
    _, i = ls.pop(0).split(':')
    i = tuple(map(int, i.split()))
    if len(ls) > 0:
        _ = ls.pop(0) # blank line
    ans = solve(g, i)
    for pair in ans:
        x, y = pair
        total += abs(x-y)
    print("Total so far is", total)

