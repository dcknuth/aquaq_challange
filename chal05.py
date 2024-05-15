# spin the dice

input = "LRUDDLRDLLDRUUUURLUDLLDLUDRURRDLUDRDURUURDLRULDULLRDRLLLDRDRRRLLDLRUUUDRLRDRLDRRUURDRLUDUUDUDLLDRULRLDRRLUUURRDDUDRDRURRLRRLLDRUUURLLRLRURRRUDUDURUDRURDRDDDURDLUDDLDUDRULDRULURLUULLLURDRLDUDRDUDRLDDRUULLLULRLDUURUUDRDLLDRRDRLLRUUURLDRULUDDRDDLDRURURR"
#input = "LRDLU"

# setup the two dice, each will just store front, left, top in order
d1 = [1, 2, 3]
d2 = [1, 3, 2]

# let's have a function for each rotation
def up(die):
    front, left, top = die
    new_front = 7 - top
    new_top = front
    die[0] = new_front
    die[2] = new_top
    return()

def down(die):
    front, left, top = die
    new_front = top
    new_top = 7 - front
    die[0] = new_front
    die[2] = new_top
    return()

def left(die):
    front, left, top = die
    new_front = 7 - left
    new_left = front
    die[0] = new_front
    die[1] = new_left
    return()

def right(die):
    front, left, top = die
    new_front = left
    new_left = 7 - front
    die[0] = new_front
    die[1] = new_left
    return()

# now do the list of rotations
total = 0
for i, rotation in enumerate(input):
    if rotation == 'U':
        up(d1)
        up(d2)
    elif rotation == 'D':
        down(d1)
        down(d2)
    elif rotation == 'L':
        left(d1)
        left(d2)
    elif rotation == 'R':
        right(d1)
        right(d2)
    else:
        print("Error: unknown rotation")
    if d1[0] == d2[0]:
        total += i

print("Sum of instruction indexes where front faces are the same is", total)
