# calculate number comfort levels
filename = 'input38.txt'
filename = 'test38.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

def streak_comfort(l):
    value_list = []
    for i in range(len(l)):
        max_run = 0
        this_run = 0
        for j in range(i+1):
            for k in range(i, len(l)):
                if sum(l[j:k+1]) % len(l[j:k+1]) == 0:
                    this_run += 1
                else:
                    if this_run > max_run:
                        max_run = this_run
                    this_run = 0
        if this_run > max_run:
            max_run = this_run
        value_list.append(max_run)
    return(sum(value_list))

total_comfort = 0
for l in ls:
    streak = list(map(int, l.split()))
    comfort = streak_comfort(streak)
    total_comfort += comfort

print(total_comfort)
