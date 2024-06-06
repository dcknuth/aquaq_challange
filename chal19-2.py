# find sum of alive cells at the end of each run
import numpy as np
from scipy.signal import convolve2d
import time

filename = "input19.txt"
#filename = "test19.txt"

with open(filename) as f:
    ls = f.read().strip().split('\n')

kernel = np.array([[0, 1, 0],
                   [1, 0, 1],
                   [0, 1, 0]])

def lifeStep(matrix, kernel):
    new_matrix = convolve2d(matrix, kernel, mode='same')
    new_matrix = np.remainder(new_matrix, 2)
    return(new_matrix)

T0 = time.perf_counter()
total = 0
for l in ls:
    points = list(map(int, l.split()))
    run_time = points.pop(0)
    grid_size = points.pop(0)
    # make grid
    m = np.zeros((grid_size, grid_size))
    # add points
    while len(points) > 0:
        y = points.pop(0)
        x = points.pop(0)
        m[y, x] = 1
    # run game of life
    for step in range(run_time):
        m = lifeStep(m, kernel)
    # count live cells
    total += np.sum(m)
    print(f"Total after line {l} is {total}")

T1 = time.perf_counter()
print(f"There are a total of {total} live cells")
print(f"The run took {T1-T0} seconds")
