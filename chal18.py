# Find the nearest palindromic times
filename = 'input18.txt'
#filename = 'test18.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

def isPalindrome(hms):
    if hms[1][0] != hms[1][1]:
        return(False)
    if hms[0] != ''.join(hms[2][::-1]):
        return(False)
    return(True)

def tickUp(hms):
    h, m, s = tuple(map(int, hms))
    if s == 59:
        hms[2] = '00'
        if m == 59:
            hms[1] = '00'
            if h == 23:
                hms[0] = '00'
            else:
                hms[0] = f'{h+1:02}'
        else:
            hms[1] = f'{m+1:02}'
    else:
        hms[2] = f'{s+1:02}'

def tickDown(hms):
    h, m, s = tuple(map(int, hms))
    if s == 0:
        hms[2] = '59'
        if m == 0:
            hms[1] = '59'
            if h == 0:
                hms[0] = '59'
            else:
                hms[0] = f'{h-1:02}'
        else:
            hms[1] = f'{m-1:02}'
    else:
        hms[2] = f'{s-1:02}'

total = 0
for l in ls:
    hour, min, sec = tuple(l.split(':'))
    tics = 0
    t_up = [hour, min, sec]
    t_down = [hour, min, sec]
    while not isPalindrome(t_up) and not isPalindrome(t_down):
        tics += 1
        tickUp(t_up)
        tickDown(t_down)
    total += tics
print("Total of all seconds away is", total)
