# find coprimes less than given number

input = 987820
#input = 15

# find the factors of our number
factors = []
for x in range(2, int(input**0.5)+1):
    if input % x == 0:
        factors.append(x)
        factors.append(round(input / x))
print("List of factors is", factors)

# now find coprimes less than our number
coprimes = [1]
for i in range(2, input):
    if i in factors:
        continue
    found = True
    for x in range(2, int(i**0.5)+1):
        if i % x == 0:
            if x in factors or round(i / x) in factors:
                found = False
                break
    if found:
        coprimes.append(i)
print("coprimes are", coprimes)

print("Sum of coprimes is", sum(coprimes))
# takes a few seconds. is there a faster way?
