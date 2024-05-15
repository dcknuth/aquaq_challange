# what is the total number of required tiles
filename = 'input11.txt'
#filename = 'test11.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

def getOverlap(r1, r2):
    x_left = max(r1[0], r2[0])
    y_bottom = max(r1[1], r2[1])
    x_right = min(r1[2], r2[2])
    y_top = min(r1[3], r2[3])
    if x_left < x_right and y_bottom < y_top:
        return([x_left, y_bottom, x_right, y_top])
    return(None)

rect_list = []
for l in ls[1:]:
    rect_list.append(list(map(int, l.split(','))))

overlap_list = []
remaining_rects = set()
for i, r in enumerate(rect_list):
    for cur_rect in rect_list[i+1:]:
        overlap = getOverlap(r, cur_rect)
        if overlap:
            overlap_list.append(overlap)
            remaining_rects.add(tuple(r))
            remaining_rects.add(tuple(cur_rect))

# since the numbers don't get too high, we can make a matrix with the
#  remaining rects and count the tiles
# print the layout and overlaps
minx = min([x[0] for x in remaining_rects])
miny = min([x[1] for x in remaining_rects]) 
maxx = max([x[2] for x in remaining_rects])
maxy = max([x[3] for x in remaining_rects])
g = [[' ' for x in range(minx, maxx)] for y in range(miny, maxy)]
for r in remaining_rects:
    for y in range(r[1], r[3]):
        for x in range(r[0], r[2]):
            g[y][x] = '#'
for r in overlap_list:
    for y in range(r[1], r[3]):
        for x in range(r[0], r[2]):
            g[y][x] = '@'
total_tiles = 0
for row in g[::-1]:
    print(''.join(row))
    total_tiles += row.count('#')
    total_tiles += row.count('@')
print("Total number of tiles needed is", total_tiles)
