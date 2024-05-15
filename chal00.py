# Numpad to text

filename = 'input00.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

np = {'0':' ',
      '2':'abc',
      '3':'def',
      '4':'ghi',
      '5':'jkl',
      '6':'mno',
      '7':'pqrs',
      '8':'tuv',
      '9':'wxyz'}

ans = []
for l in ls:
    n, m = l.split()
    ans.append(np[n][int(m)-1])
print("Answer is\n", ''.join(ans))
