# find all the numbers whose digits are not decreasing
input = 520185742
#input = 1000000

n = 0
count = 0
while n <= input:
    digits = [d for d in str(n)]
    d_sorted = sorted(digits)
    if digits == d_sorted:
        count += 1
    n += 1

print(f"There are {count} increasing numbers up to {input}")
