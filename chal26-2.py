# change the number into the next biggest number with the same digits
filename = 'input26.txt'
#filename = 'test26.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

def findNext(n):
    num = int(n)
    orig = [c for c in n]
    orig_sorted = tuple(sorted(orig, reverse=True))
    if num == int(''.join(orig_sorted)):
        return(num)
    found = False
    while not found:
        num += 1
        cur = [c for c in str(num)]
        cur.sort(reverse=True)
        if orig_sorted == tuple(cur):
            return(num)

orig = [int(x) for x in ls]
rewritten = []
gains = 0
for i, l in enumerate(ls):
    next = findNext(l)
    rewritten.append(next)
    gains += next - orig[i]
    print(f"Orig {orig[i]} next {next} gain so far {gains}")

print("Our total gains are", gains)
