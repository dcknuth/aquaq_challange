# what is my remaining milk and cereal
# in order to get this to come out correctly, you need to assume you are
#  on your first shopping trip for cereal the day after the last input and
#  not on the second shopping trip for milk after eating cereal
filename = 'input08.txt'
#filename = 'test08.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

my_milk = [0 for x in range(5)]
my_cereal = 0

#print("day milk cereal")
#print("---------------")
d_num = 1
for day in ls[1:]:
    cur_date, milk_added, cereal_added = day.split(',')
    milk_added = int(milk_added)
    cereal_added = int(cereal_added)
    # shop for cereal
    my_cereal += cereal_added
    # eat breakfast
    if sum(my_milk) > 0 and my_cereal > 0:
        my_cereal -= 100
        i = 0
        while i < len(my_milk):
            if my_milk[i] > 0:
                my_milk[i] -= 100
                break
            i += 1
    # expire the milk
    my_milk.pop(0)
    # add today's milk purchase
    my_milk.append(milk_added)
    #print(f"{d_num:<3} {sum(my_milk):<4} {my_cereal:<4}")
    d_num += 1

# last day, need to assume beginning of day to get the right answer
print("Remaining weight of milk and cereal is",
      sum(my_milk) + my_cereal)
