# find sum of alive cells at the end of each run
import time

filename = "input19.txt"
#filename = "test19.txt"

with open(filename) as f:
    ls = f.read().strip().split('\n')

def lifeStep(g):
    new_grid = []
    y = 0
    while y < len(g):
        x = 0
        cur_row = []
        while x < len(g[y]):
            count = 0
            if y > 0 and g[y-1][x] == '#':
                count += 1
            if x > 0 and g[y][x-1] == '#':
                count += 1
            if x + 1 < len(g[y]) and g[y][x+1] == '#':
                count += 1
            if y + 1 < len(g) and g[y+1][x] == '#':
                count += 1
            if count % 2 == 0:
                cur_row.append('.')
            else:
                cur_row.append('#')
            x += 1
        new_grid.append(cur_row)
        y += 1
    return(new_grid)

T0 = time.perf_counter()
total = 0
for l in ls:
    points = list(map(int, l.split()))
    run_time = points.pop(0)
    grid_size = points.pop(0)
    # make grid
    g = [['.' for x in range(grid_size)] for y in range(grid_size)]
    # add points
    while len(points) > 0:
        y = points.pop(0)
        x = points.pop(0)
        g[y][x] = '#'
    # run game of life
    for step in range(run_time):
        g = lifeStep(g)
    # count live cells
    for y in g:
        cur_row = ''.join(y)
        total += cur_row.count('#')
    print(f"Total after line {l} is {total}")

T1 = time.perf_counter()
print(f"There are a total of {total} live cells")
print(f"The run took {T1-T0} seconds")
