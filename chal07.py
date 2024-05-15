# find difference of best - worst elo score after series of matches
# this helps: https://en.wikipedia.org/wiki/Elo_rating_system
filename = 'input07.txt'
#filename = 'test07.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

def pointsToWinner(win_expectation, K=20):
    return(K * (1 - win_expectation))

def chanceOfWin(rank_winner, rank_loser):
    return(1 / (1 + 10 ** ((rank_loser - rank_winner)/400)))

elos = dict()
for g in ls[1:]:
    h, a, score = g.split(',')
    h_score, a_score = list(map(int, score.split('-')))
    if h in elos:
        h_elo = elos[h]
    else:
        h_elo = 1200
    if a in elos:
        a_elo = elos[a]
    else:
        a_elo = 1200
    if h_score > a_score:
        percent = chanceOfWin(h_elo, a_elo)
        points_moved = pointsToWinner(percent)
        elos[h] = h_elo + points_moved
        elos[a] = a_elo - points_moved
    elif a_score > h_score:
        percent = chanceOfWin(a_elo, h_elo)
        points_moved = pointsToWinner(percent)
        elos[a] = a_elo + points_moved
        elos[h] = h_elo - points_moved
    else:
        # tie case, which we don't seem to have
        elos[h] = h_elo
        elos[a] = a_elo

final_ranks = list(elos.values())
final_ranks.sort()
print("High to low difference is", int(final_ranks[-1]) - int(final_ranks[0]))


