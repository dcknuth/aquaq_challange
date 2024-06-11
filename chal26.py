# change the number into the next biggest number with the same digits
filename = 'input26.txt'
#filename = 'test26.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

def findNext(n):
    orig = list(n)
    reverse = orig[::-1]
    found = False
    for i in range(1, len(reverse)):
        search_set = reverse[:i]
        for j, digit in enumerate(search_set):
            if digit > reverse[i]:
                # swap and sort
                remaining = reverse[i+1:]
                save = reverse[i]
                new_reverse = search_set.copy()
                new_reverse[j] = save
                new_reverse.sort(reverse=True)
                new_reverse.append(digit)
                new_reverse.extend(remaining)
                found = True
                break
        if found:
            break
    if not found:
        return(int(n))
    new_n = new_reverse[::-1]
    return(int(''.join(new_n)))

orig = [int(x) for x in ls]
rewritten = []
gains = 0
for i, l in enumerate(ls):
    next = findNext(l)
    rewritten.append(next)
    gains += next - orig[i]
    print(f"Orig {orig[i]} next {next} gain so far {gains}")

print("Our total gains are", gains)
