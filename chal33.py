# play games of darts up to the given number. How many darts are needed
points = 245701
#points = 30

# make a list of all possible points
plist = list(range(1, 21))
plist.extend([x * 2 for x in range(1, 21)])
plist.extend([x * 3 for x in range(1, 21)])
plist.extend([25, 50])
plist = set(plist)

total_darts = 0
for game in range(1, points+1):
    cur_darts = game // 60
    remaining = game - cur_darts * 60
    if remaining in plist:
        cur_darts += 1
    else:
        cur_darts += 2
    total_darts += cur_darts
print("Total darts used is", total_darts)

# This does not work as there are some numbers > 60 that can be shifted a
#  little to save one dart. Like 83; instead of 60 + 22 + 1 one could throw
#  57 + 26. Now, how to figure out all our cases where this could be done.
#  I suspect this comes into play for remainders between 23 and 59.
# Remainders of // 60 that fall into this would be 23, 29, 31, 35, 37, 41,
#  44 and 47. Not 43, 46, 49, 52, 53, 55, 56, 58 and 59, which would
#  still need two darts for the remainder.
# Let's try that

total_darts = 0
for game in range(1, points+1):
    cur_darts = game // 60
    remaining = game - cur_darts * 60
    if cur_darts > 0:
        if remaining in [43, 46, 49, 52, 53, 55, 56, 58, 59]:
            cur_darts += 2
        else:
            cur_darts += 1
    elif cur_darts == 0:
        if remaining in plist:
            cur_darts += 1
        else:
            cur_darts += 2
    #print(f"cur target is {game} and # darts is {cur_darts}")
    total_darts += cur_darts
print("Total darts used (updated) is", total_darts)
# Nope, still something wrong. The low difficulty rating says I am missing
#  something easy

# Next, let's try all combinations of N//60 + 1 (if % 60 not 0) and if there
#  is not one that works, we need N//60 + 2 darts
from itertools import combinations
# total_darts = 0
# for game in range(1, points+1):
#     num_darts = game // 60
#     if game % 60 == 0:
#         total_darts += num_darts
#     else:
#         num_darts += 1
#         found = False
#         points_list = combinations(plist, num_darts)
#         for cur_points in points_list:
#             if sum(cur_points) == game:
#                 found = True
#                 break
#         if not found:
#             num_darts += 1
#     print(f"cur target is {game} and # darts is {num_darts}")
#     total_darts += num_darts
# print("Total darts is", total_darts)
# way too slow and not working correctly

# Another version of the second method
total_darts = 0
for game in range(1, points+1):
    cur_darts = game // 60
    remaining = game - cur_darts * 60
    if remaining == 0:
        pass
    elif cur_darts > 0 and remaining in plist:
        cur_darts += 1
    elif cur_darts == 0:
        if remaining in plist:
            cur_darts += 1
        else:
            cur_darts += 2
    else:
        found = False
        combos = combinations(plist, 2)
        for combo in combos:
            if 60 + remaining == sum(combo):
                found = True
                break
        if found:
            cur_darts += 1
        else:
            cur_darts += 2
    #print(f"cur target is {game} and # darts is {cur_darts}")
    total_darts += cur_darts
print("Total darts is", total_darts)
# now working, but we can probably go a little faster

alternates = dict()
combos = combinations(plist, 2)
for combo in combos:
    alternates[sum(combo)] = True
total_darts = 0
for game in range(1, points+1):
    cur_darts = game // 60
    remaining = game - cur_darts * 60
    if remaining == 0:
        pass
    elif cur_darts > 0 and remaining in plist:
        cur_darts += 1
    elif cur_darts == 0:
        if remaining in plist:
            cur_darts += 1
        else:
            cur_darts += 2
    else:
        if 60 + remaining in alternates:
            cur_darts += 1
        else:
            cur_darts += 2
    total_darts += cur_darts
print("Total darts is", total_darts)
# yep, way faster
