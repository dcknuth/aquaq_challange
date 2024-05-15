# break into sums and count '1's

input = 123
#input = 3

total = 0
# try all numbers up to the input in the first position
for x in range(input+1):
    # then up to the input minus the current number in the second position
    for y in range((input+1)-x):
        # the third number can be calculated
        z = (input - x) - y
        s = ''.join(map(str, [x, y, z]))
        total += s.count('1')

print("Number of '1's that appear is", total)
