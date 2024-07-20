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
        # count up the longest run where exactly one number is added to one
        #  of the ends. We will need to start from each list and count up
        #  lengths. So we will need a grouping of the comfortable lists by
        #  list lengths TODO try without the early stop, with longest from
        #  any start
        by_length = defaultdict(list)
        for s in comfortable:
            by_length[len(s[0])].append(s)
        longest = 0
        if 1 in by_length:
            possible_streaks = [[deepcopy(by_length[1][0])]]
        else:
            continue
        append_length = 2
        while len(by_length[append_length]) > 0:
            new_possible = []
            for y in possible_streaks:
                for z in by_length[append_length]:
                    temp_list = deepcopy(y)
                    temp_list.append(deepcopy(z))
                    new_possible.append(temp_list)
            append_length += 1
            possible_streaks = new_possible
        # now we should be able to test each streak
        for streak_list in possible_streaks:
            last_streak = streak_list[0]
            this_length = 1
            for streak in streak_list[1:]:
                if streak[1][:-1] == last_streak[1] or \
                        streak[1][1:] == last_streak[1]:
                    this_length += 1
                    last_streak = streak
                else:
                    break
            if longest < this_length:
                longest = this_length
        streaks.append(cur_streaks)
        total_comfort += longest
    return(total_comfort)

all_lists_comfort = 0
for l in ls:
    l = list(map(int, l.split()))
    list_comfort = gen_streaks(l)
    all_lists_comfort += list_comfort
    print(l)
    print(list_comfort, all_lists_comfort)


