# move around the room

input = 'LDRDLRDRDDRLRLDLLLUULURURLDULUUDRRDDRUDDRLRRULRDUDRUDRRLRDLDRULLDUUULDRRLDDLURLURRURLRLRUULDULDLLLUDLULDUUUDLDLLUUULDDLUURDUDDRULRULRULRDULRULULRLRDRDRULLRDRRRULLRDRDDRDULDDDUUDDRDRLRRRUUDDDULULLULURURLURULRDRUDLULRULLRRLLLRRRLRRLUULDUUUULLRDRRUULULURRURDRLDLLRUDULDRULDDRURLDRDLRRULRDRRUDRURULDURRULDLDULRLLLRLUURDLUUURUDLRLUUULULULUDRRDRUDLUDLRUUUDRRDDLLUDLDURDLRRRDRDLRLRRUDLRDRUUDULLDDRRUUDDRDRDLDRLLRRRUDLRDRUDDRURLLLDDLRRDUDDUDULURDLULDDLDRRRLLLRLDUURDUDULDDRRDRDLLDRDRRLLULLLRLURLLDDLDLRDUUUDR'
#input = 'UDRR'
room = ['  ##  ',
        ' #### ',
        '######',
        '######',
        ' #### ',
        '  ##  ']
cury = 0
curx = 2

# move through the room while summing position indexes
total = 0
for d in input:
    if d == 'U':
        newy = cury - 1
        newx = curx
    elif d == 'D':
        newy = cury + 1
        newx = curx
    elif d == 'L':
        newx = curx - 1
        newy = cury
    elif d == 'R':
        newx = curx + 1
        newy = cury
    else:
        print('Bad direction encountered')
        exit()
    if newy < 0 or newy > 5 or newx < 0 or newx > 5:
        # outside the array
        total += cury + curx
        continue
    if room[newy][newx] == ' ':
        # outside the #s
        total += cury + curx
        continue
    cury = newy
    curx = newx
    total += cury + curx

print("Sum of indexes is", total)
