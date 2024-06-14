# encrypt using a changing hall of mirrors
filename = 'input28.txt'
#filename = 'test28.txt'
plain_text = 'FISSION_MAILED'
#plain_text = 'DAD'

with open(filename) as f:
    ls = f.read().split('\n')

m = []
for l in ls[:-1]:
    row = [c for c in l]
    m.append(row)
valid_text = m[0][1:-1]

def moveOne(m, y, x, d):
    if d == 'R':
        x += 1
    elif d == 'L':
        x -= 1
    elif d == 'U':
        y -= 1
    elif d == 'D':
        y += 1
    else:
        print(f"Error: direction {d}")
    if m[y][x] == ' ':
        return(y, x, d)
    if m[y][x] == '/':
        m[y][x] = '\\'
        if d == 'R':
            return(y, x, 'U')
        if d == 'L':
            return(y, x, 'D')
        if d == 'U':
            return(y, x, 'R')
        if d == 'D':
            return(y, x, 'L')
        else:
            print(f"Error: {y}, {x}, {d}")
            return(0, 0, d)
    if m[y][x] == '\\':
        m[y][x] = '/'
        if d == 'R':
            return(y, x, 'D')
        if d == 'L':
            return(y, x, 'U')
        if d == 'U':
            return(y, x, 'L')
        if d == 'D':
            return(y, x, 'R')
        else:
            print(f"Error: {y}, {x}, {d}")
            return(0, 0, d)
    if m[y][x] in valid_text:
        return(y, x, d)
    else:
        print(f"Error: {y}, {x}, {d}")
        return(0, 0, d)

encrypted = []
for c in plain_text:
    # set start y position
    for i in range(1, len(m)-1):
        if c == m[i][0]:
            y = i
            break
    y, x, d = moveOne(m, y, 0, 'R')
    while y != 0 and x != 0 and y != len(m)-1 and x != len(m[0])-1:
        y, x, d = moveOne(m, y, x, d)
    encrypted.append(m[y][x])

print("Encrypted text is", ''.join(encrypted))
