# try to remove all cards via face up removals and adjacent flips
from functools import lru_cache
filename = 'input30.txt'
#filename = 'test30.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

@lru_cache(maxsize=100000000)
def canWin(hand):
    if hand == (True,):
        return(True)
    if hand == (False,):
        return(False)
    if True not in hand:
        return(False)
    win_found = False
    for i in range(len(hand)):
        if hand[i]:
            if i == 0:
                new_hand = (not hand[1],) + hand[2:]
                win_found = canWin(new_hand)
            elif i == len(hand) - 1:
                new_hand = hand[:-2] + (not hand[-2],)
                win_found = canWin(new_hand)
            else:
                p1 = hand[:i-1] + (not hand[i-1],)
                p2 = (not hand[i+1],) + hand[i+2:]
                win_found = canWin(p1) and canWin(p2)
            if win_found:
                break
    return(win_found)

total = 0
for l in ls:
    cur_total = 0
    orig = [x == '1' for x in l]
    if len(orig) < 2 and canWin(tuple(orig)):
        cur_total += 1
    for i in range(len(orig)):
        if orig[i]:
            if i == 0:
                new_list = orig[i+1:]
                new_list[0] = not new_list[0]
                if canWin(tuple(new_list)):
                    cur_total += 1
                continue
            if i == len(orig) - 1:
                new_list = orig[:i]
                new_list[-1] = not new_list[-1]
                if canWin(tuple(new_list)):
                    cur_total += 1
                continue
            else:
                p1 = orig[:i]
                p1[-1] = not p1[-1]
                p2 = orig[i+1:]
                p2[0] = not p2[0]
                if canWin(tuple(p1)) and canWin(tuple(p2)):
                    cur_total += 1
    print(l, cur_total)
    total += cur_total

print("Sum of win positions is", total)
