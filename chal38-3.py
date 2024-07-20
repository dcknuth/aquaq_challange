# calculate number comfort levels
from collections import defaultdict
from copy import deepcopy
filename = 'input38.txt'
#filename = 'test38.txt'
#filename = 'test38-2.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

def gen_streaks(l):
    total_comfort = 0
    streaks = []
    for x in range(len(l)):
        # generate all lists for the current number
        cur_streaks = defaultdict(list)
        for i in range(0, len(l)):
            j = x - i
            if j < 0:
                j = 0
            k = j + i + 1
            while j <= x and k <= len(l):
                cur_streak = l[j:k]
                cur_indexes = list(range(j, k))
                cur_streaks[sum(cur_streak)].append([cur_streak, cur_indexes])
                j += 1
                k += 1
        # sort them by sum
        keys = list(cur_streaks.keys())
        keys.sort()
        # eval for comfort in that order, dropping any that are uncomfortable
        comfortable = []
        for key in keys:
            for streak in cur_streaks[key]:
                if key % len(streak[0]) == 0:
                    comfortable.append(streak)
        # this time we will count runs of comfortable lengths. So we will need
        #  a grouping of the comfortable lists by list lengths and restart
        #  the count when there are no comfortable runs of the next length
        by_length = defaultdict(list)
        for s in comfortable:
            by_length[len(s[0])].append(s)
        longest = 0
        keys = list(by_length.keys())
        keys.sort()
        cur_run_len = 1
        last_len = keys[0]
        for key in keys[1:]:
            if key - last_len == 1:
                cur_run_len += 1
            else:
                if longest < cur_run_len:
                    longest = cur_run_len
                cur_run_len = 1
            last_len = key
        if longest < cur_run_len:
            longest = cur_run_len
        total_comfort += longest
    return(total_comfort)

all_lists_comfort = 0
for l in ls:
    l = list(map(int, l.split()))
    list_comfort = gen_streaks(l)
    all_lists_comfort += list_comfort
    print(l)
    print(list_comfort, all_lists_comfort)


