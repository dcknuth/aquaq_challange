# try to remove all cards via face up removals and adjacent flips
from functools import lru_cache
filename = 'input30.txt'
#filename = 'test30.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

@lru_cache(maxsize=100000000)
def isWinable(hand):
    if hand == '1' or hand == '10' or hand == '01':
        return(True)
    if hand == '0' or hand == '00' or hand == '11':
        return(False)
    if '1' not in hand:
        return(False)
    win_found = False
    for i in range(len(hand)):
        if hand[i] == '0':
            continue
        # 1 is in this position
        if i == 0:
            if hand[i+1] == '0':
                new_hand = '1' + hand[2:]
            else:
                new_hand = '0' + hand[2:]
            win_found = isWinable(new_hand)
        elif i == len(hand) - 1:
            if hand[-2] == '0':
                new_hand = hand[:-2] + '1'
            else:
                new_hand = hand[:-2] + '0'
            win_found = isWinable(new_hand)
        else:
            if hand[i-1] == '0':
                p1 = hand[:i-1] + '1'
            else:
                p1 = hand[:i-1] + '0'
            if hand[i+1] == '0':
                p2 = '1' + hand[i+2:]
            else:
                p2 = '0' + hand[i+2:]
            win_found = isWinable(p1) and isWinable(p2)
        if win_found:
            break
    return(win_found)

total_wins = 0
for l in ls:
    winable_positions = 0
    if len(l) == 1:
        if l == '1':
            winable_positions = 1
    else:
        for i, c in enumerate(l):
            if c == '0':
                continue
            if i == 0:
                if l[1] == '0':
                    new_hand = '1' + l[2:]
                else:
                    new_hand = '0' + l[2:]
                if isWinable(new_hand):
                    winable_positions += 1
                continue
            if i == len(l) - 1:
                if l[-2] == '0':
                    new_hand = l[:-2] + '1'
                else:
                    new_hand = l[:-2] + '0'
                if isWinable(new_hand):
                    winable_positions += 1
                continue
            p1 = l[:i-1]
            if l[i-1] == '0':
                p1 = p1 + '1'
            else:
                p1 = p1 + '0'
            p2 = l[i+2:]
            if l[i+1] == '0':
                p2 = '1' + p2
            else:
                p2 = '0' + p2
            if isWinable(p1) and isWinable(p2):
                winable_positions += 1
    print(f"hand {l} has {winable_positions} winable positions")
    total_wins += winable_positions
    print(isWinable.cache_info())

print("Sum of winable positions is", total_wins)
