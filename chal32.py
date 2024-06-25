# how many lines have balenced braces
filename = 'input32.txt'
#filename = 'test32.txt'
OPEN = ['(', '[', '{']
CLOSE = [')', ']', '}']

with open(filename) as f:
    ls = f.read().strip().split('\n')

total = 0
for l in ls:
    l = list(l)
    stack = []
    balanced = True
    while len(l) > 0:
        c = l.pop(0)
        if c in CLOSE:
            if len(stack) > 0:
                if c == ')' and stack[-1] == '(':
                    stack.pop()
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                elif c == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    balanced = False
                    break
            else:
                balanced = False
                break
        elif c in OPEN:
            stack.append(c)
    if balanced and len(stack) == 0:
        total += 1

print("Total balanced rows is", total)
