# multiply winning darts and the number of wins
filename = 'input39.txt'
#filename = 'test39.txt'

with open(filename) as f:
    ls = f.read().strip().split()

last_darts = []
winner = []
cur_scores = [0, 0]
current_player = 0
next_starter = 1
someone_won = False
while len(ls) > 0:
    for i in range(3):
        l = ls.pop(0)
        d = int(l)
        cur_scores[current_player] += d
        if cur_scores[current_player] == 501:
            last_darts.append(d)
            if current_player == 0:
                winner.append('A')
            else:
                winner.append('B')
            cur_scores = [0, 0]
            current_player = next_starter
            if next_starter == 1:
                next_starter = 0
            else:
                next_starter = 1
            someone_won = True
            break
    if someone_won:
        someone_won = False
        continue
    else:
        if current_player == 1:
            current_player = 0
        else:
            current_player = 1

print(sum(last_darts) * ''.join(winner).count('A'))
