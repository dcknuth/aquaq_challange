# text to color attribute

filename = 'input01.txt'
HEX_DIGITS = '0123456789abcdef'

with open(filename) as f:
    s = f.read().strip()

#s = 'kdb4life'
# set non-hex to 0
with_zeros = []
for c in s:
    if c in HEX_DIGITS:
        with_zeros.append(c)
    else:
        with_zeros.append('0')

# pad
while len(with_zeros) % 3 != 0:
    with_zeros.append('0')

# split and take first two
final = with_zeros[:2]
sec_len = len(with_zeros)//3
final.extend(with_zeros[sec_len:sec_len+2])
final.extend(with_zeros[sec_len*2:sec_len*2+2])

print(''.join(final))
