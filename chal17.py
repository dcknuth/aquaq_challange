# Find the team with the longest no-goal streak and the dates
from datetime import datetime, timedelta
from collections import defaultdict
filename = 'input17.txt'
#filename = 'test17.txt'

with open(filename, 'r', encoding='utf-8') as f:
    ls = f.read().strip().split('\n')

active_streaks = dict()
finished_streaks = defaultdict(list)
longest = [0, '', '', '']
cur_day = datetime(year=1872, month=11, day=1).date()
end_day = datetime(year=2018, month=6, day=25).date()
games = []
for l in ls[1:]:
    game = l.split(',')
    games.append(game)

games.sort()
for game in games:
    d, ht, at, hs, away_score, tour, c, cn, n = game
    if hs == '0':
        if ht not in active_streaks:
            year, month, day = list(map(int, d.split('-')))
            start = datetime(year=year, month=month, day=day).date()
            active_streaks[ht] = start
    else:
        if ht in active_streaks:
            year, month, day = list(map(int, d.split('-')))
            finish = datetime(year=year, month=month, day=day).date()
            start = active_streaks[ht]
            diff = finish - start
            finished_streaks[ht].append([ht, start.strftime("%Y%m%d"),
                                         finish.strftime("%Y%m%d"), diff.days])
            if diff.days > longest[0]:
                longest[0] = diff.days
                longest[1] = ht
                longest[2] = start.strftime("%Y%m%d")
                longest[3] = finish.strftime("%Y%m%d")
            del(active_streaks[ht])
    if away_score == '0':
        if at not in active_streaks:
            year, month, day = list(map(int, d.split('-')))
            start = datetime(year=year, month=month, day=day).date()
            active_streaks[at] = start
    else:
        if at in active_streaks:
            year, month, day = list(map(int, d.split('-')))
            finish = datetime(year=year, month=month, day=day).date()
            start = active_streaks[at]
            diff = finish - start
            finished_streaks[at].append([ht, start.strftime("%Y%m%d"),
                                         finish.strftime("%Y%m%d"), diff.days])
            if diff.days > longest[0]:
                longest[0] = diff.days
                longest[1] = at
                longest[2] = start.strftime("%Y%m%d")
                longest[3] = finish.strftime("%Y%m%d")
            del(active_streaks[at])

print(f"Longest shame is {longest[1]} {longest[2]} {longest[3]}")
