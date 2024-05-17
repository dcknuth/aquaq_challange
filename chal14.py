# play bingo, sum numbers until a win in each line
#  we are assuming a square board and no repeated numbers
from collections import Counter
filename = 'input14.txt'
#filename = 'test14.txt'

board = [[6, 17, 34, 50, 68],
         [10, 21, 45, 53, 66],
         [5, 25, 36, 52, 69],
         [14, 30, 33, 54, 63],
         [15, 23, 41, 51, 62]]

def doWeWin(board, matches, groups):
    if len(matches) < len(board):
        return("No")
    for rcd in groups.keys():
        if groups[rcd] >= len(board):
            return(rcd)
    return("No")

def placeOnBoard(board, matches, groups, n):
    for y in range(len(board)):
        for x in range(len(board)):
            if n == board[y][x]:
                matches.append(n)
                groups[f'R{y}'] += 1
                groups[f'C{x}'] += 1
                if y == x:
                    groups['DD'] += 1
                if y + x == len(board) - 1:
                    groups['DU'] += 1

with open(filename) as f:
    ls = f.read().strip().split('\n')

total_draws = 0
for l in ls:
    matches = []
    groups = Counter()
    cur_game = [int(x) for x in l.split()]
    for i, n in enumerate(cur_game):
        placeOnBoard(board, matches, groups, n)
        result = doWeWin(board, matches, groups)
        if result != 'No':
            total_draws += i + 1
            print("Win in", result)
            break

print("Total draws needed for all games is", total_draws)
