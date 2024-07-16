# solve the math puzzles (tetonors) and sum up the answers
from collections import defaultdict
from copy import deepcopy
filename = 'input36.txt'
#filename = 'test36.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

def last_num(i, a):
    step = 1
    while a - step >= 0:
        if i[a-step] != '*':
            return(int(i[a-step]))
        step += 1
    return(1)

def next_num(i, a, max_g):
    step = 1
    while a + step < len(i):
        if i[a+step] != '*':
            return(int(i[a+step]))
        step += 1
    return(max_g)

def find_factors(n):
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    factors.append(n)
    factors.sort()
    return factors

def make_combos(g, i, i_ints, all_pairs, wc_ranges, prod_possibles):
    '''Make combo lists for the numbers that we have and store inclusive
    ranges for where our wild cards could be'''
    max_g = max(g)
    for a, j in enumerate(i):
        if len(j) == 2:
            wc_min, wc_max = j
            wc_ranges.append((wc_min, wc_max))
            continue
        x = j[0]
        i_ints.append(x)
        for b in i[a+1:]:
            if len(b) == 2:
                continue
            y = b[0]
            if x + y in g and x * y in g:
                all_pairs[x+y].add((x, y))
                all_pairs[x*y].add((x, y))
    # now we need valid values for the ranges
    # since two numbers need to multiply to be in g a valid number has
    #  to be a factor of something in g. Let's find the factors and make a
    #  dictionary for those
    all_factors = defaultdict(list)
    for num in g:
        factors = find_factors(num)
        for factor in factors:
            all_factors[factor].append(num)
    # now filter possibilities
    for a, pair in enumerate(wc_ranges):
        low, high = pair
        for num in range(low, high+1):
            if num in all_factors:
                for target in all_factors[num]:
                    partner = target // num
                    if partner in i_ints and num + partner in g:
                        # add to possibles
                        prod_possibles[pair].append((num, partner))
                    else:
                        # search the other ranges for possibles and add
                        #  if found
                        for b, pair2 in enumerate(wc_ranges):
                            if b == a:
                                continue
                            low2, high2 = pair2
                            if partner >= low2 and partner <= high2:
                                if num + partner in g:
                                    prod_possibles[pair].append((num, partner))
    # Now add to our list of all possible ways to get the values in g
    for min_max in wc_ranges:
        for pair in prod_possibles[min_max]:
            x, y = pair
            if x > y:
                pair = (y, x)
            all_pairs[x+y].add(pair)
            all_pairs[x*y].add(pair)

def i_remove(i, x):
    '''remove a number from the input list of i'''
    found = False
    remove_index = -1
    for a, cur_i in enumerate(i):
        if len(cur_i) == 1:
            if cur_i[0] == x:
                found = True
                remove_index = a
                break
    if found:
        i.pop(remove_index)
    else:
        for a, cur_i in enumerate(i):
            if len(cur_i) == 2:
                low, high = cur_i
                if x >= low and x <= high:
                    remove_index = a
                    break
        i.pop(remove_index)

def solve_remaining(g, i, all_pairs):
    '''Solve from a given state with a next pair to try. Return an answer
    list or empty list if this path fails'''
    for num in all_pairs.keys():
        for pair in all_pairs[num]:
            g_new = g.copy()
            i_new = deepcopy(i)
            x, y = pair
            answer_set = [(x, y)]
            if x + y == num:
                g_new.remove(num)
                g_new.remove(x * y)
            else:
                g_new.remove(num)
                g_new.remove(x + y)
            i_remove(i_new, x)
            i_remove(i_new, y)
            ans = solve(g_new, i_new)
            if len(ans) == len(g_new):
                return(answer_set.extend(ans))
    return([])
            
        

def solve(g, i):
    '''We need to look at our possible pairs, choose one that we have to
    and then remove what we used and then do it again until all in g
    are found'''
    answer_set = []
    g_left = list(g)
    i_left = deepcopy(i)
    while len(g_left) > 0:
        all_pairs = defaultdict(set)
        prod_possibles = defaultdict(list)
        wc_ranges = []
        g_needed = defaultdict(int)
        i_ints = []
        # count up the number of each number in g
        for num in g_left:
            g_needed[num] += 1
        make_combos(g_left, i_left, i_ints, all_pairs, wc_ranges,
                    prod_possibles)
        # remove numbers that only have the number of pair types they need
        g_remove_list = []
        i_remove_list = []
        found_force = False
        for num in all_pairs.keys():
            if len(all_pairs[num]) == g_needed[num]:
                x, y = next(iter(all_pairs[num]))
                answer_set.append((x, y))
                if x + y == num:
                    g_remove_list.append(num)
                    g_remove_list.append(x * y)
                else:
                    g_remove_list.append(num)
                    g_remove_list.append(x + y)
                i_remove_list.extend([x, y])
                found_force = True
                break
        if found_force == False:
            ans = solve_remaining(g_left, i_left, all_pairs)
            answer_set.extend(ans)
            return(answer_set)
        for num in g_remove_list:
            g_left.remove(num)
        for num in i_remove_list:
            i_remove(i_left, num)
    return(answer_set)


# loop through puzzles and sum up
total = 0
while len(ls) > 0:
    _, g = ls.pop(0).split(':')
    g = tuple(map(int, g.split()))
    _, i = ls.pop(0).split(':')
    i = i.split()
    if len(ls) > 0:
        _ = ls.pop(0) # blank line
    # prep i
    i_left = []
    max_g = max(g)
    for a, num in enumerate(i):
        if num != '*':
            i_left.append([int(num)])
        else:
            low = last_num(i, a)
            high = next_num(i, a, max_g)
            i_left.append([low, high])
    ans = solve(g, i_left)
    for pair in ans:
        x, y = pair
        total += abs(x-y)
    print("Total so far is", total)

