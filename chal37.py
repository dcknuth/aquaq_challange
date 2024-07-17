# solve a bunch of Wordles
# successive guesses do not seem to remove 2s, so assuming that
# same with 1s, assuming to keep until fixed with a 2
from collections import defaultdict, Counter
import re
filename = 'input37.txt'
#filename = 'test37.txt'
#filename = 'test37-2.txt'
word_file = 'words.txt'

with open(word_file) as f:
    words = f.read().strip().split('\n')
words = [w for w in words if len(w) == 5]
with open(filename) as f:
    ls = f.read().strip().split('\n')

def reduce_set(cur_set, not_in_pos, not_in_free, guess, result):
    new_set = []
    in_free = set()
    result = result.split()
    fixed = ['.' for x in range(5)]
    pattern = fixed.copy()
    process_not_in = []
    for i, c in enumerate(guess):
        if result[i] == '2':
            pattern[i] = c
            fixed[i] = c
        elif result[i] == '1':
            not_in_pos[i].add(c)
            in_free.add(c)
            exclude_text = '|'.join(not_in_pos[i])
            pattern[i] = f'[^{exclude_text}]'
        else:
            process_not_in.append(c)
    free_list = []
    for i, c in enumerate(fixed):
        if c == '.':
            free_list.append(i)
    for c in process_not_in:
        if c in in_free:
            # only count out the exact slot listed
            for j, d in enumerate(guess):
                if d == c and result[j] == '0':
                    not_in_free[c].add(j)
            # and any other that is 0 due to another repeat
            counts = Counter()
            for j, d in enumerate(guess):
                if d != c:
                    counts[d] += 1
                    if counts[d] > 1:
                        not_in_free[c].add(j)
        else:
            not_in_free[c] = set(free_list.copy())
    pat = ''.join(pattern)
    for word in cur_set:
        short_out = False
        for c in not_in_free.keys():
            free_vals = []
            for i in not_in_free[c]:
                free_vals.append(word[i])
            if c in free_vals:
                short_out = True
                break
        if short_out:
            continue
        for c in in_free:
            free_vals = []
            for i, x in enumerate(fixed):
                if x == '.':
                    free_vals.append(word[i])
            if c not in free_vals:
                short_out = True
                break
        if short_out:
            continue
        match = re.match(pat, word)
        if match:
            new_set.append(word)
    return(new_set)

total = 0
cur_set = []
new_word = True
last_result_t = 0
for l in ls[1:]:
    guess, result = l.split(',')
    cur_result_t = sum(map(int, result.split()))
    if cur_result_t < last_result_t and not new_word:
        print("Warning: we might have missed something", guess, result)
    if new_word:
        not_in_pos = defaultdict(set)
        not_in_free = defaultdict(set)
        cur_set = words.copy()
        new_word = False
    cur_set = reduce_set(cur_set, not_in_pos, not_in_free, guess, result)
    last_result_t = cur_result_t
    if len(cur_set) == 1:
        cur_total = 0
        for c in cur_set[0]:
            cur_total += ord(c) - ord('a')
        print(f"The current word is {cur_set[0]} with {cur_total} points")
        total += cur_total
        new_word = True

print("Sum of word points is", total)
