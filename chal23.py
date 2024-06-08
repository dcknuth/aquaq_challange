# use the Playfair cipher to decrypt
import string

input = 'vepcundbyoaeirotivluxnotpstfnbwept'
#input = 'pabapgxyxy'
keyword = 'power plant'
#keyword = 'playfair'

def make_cgrid(keyword):
    cgrid = []
    alphabet = string.ascii_lowercase
    # we are told not to use j
    alphabet = alphabet.replace('j', '')
    # remove spaces from keyword
    keyword = keyword.replace(' ', '')
    for c in keyword:
        if c in cgrid:
            continue
        cgrid.append(c)
        alphabet = alphabet.replace(c, '')
    cgrid.extend(list(alphabet))
    return([cgrid[x*5:x*5+5] for x in range(5)])

def decrypt(cipher_text, cgrid):
    plain_text = []
    ct_list = list(cipher_text)
    while len(ct_list) > 0:
        # two letters as a time
        l1 = ct_list.pop(0)
        l2 = ct_list.pop(0)
        l1y = l1x = l2y = l2x = 0
        for i in range(5):
            if l1 in cgrid[i]:
                l1y = i
                l1x = cgrid[i].index(l1)
            if l2 in cgrid[i]:
                l2y = i
                l2x = cgrid[i].index(l2)
        # if on same row, letter to the left
        if l1y == l2y:
            plain_text.append(cgrid[l1y][(l1x-1)%5])
            plain_text.append(cgrid[l2y][(l2x-1)%5])
        # if on same column, letter above
        elif l1x == l2x:
            plain_text.append(cgrid[(l1y-1)%5][l1x])
            plain_text.append(cgrid[(l2y-1)%5][l2x])
        # else, opposite row-wise side of box formed by letters
        else:
            plain_text.append(cgrid[l1y][l2x])
            plain_text.append(cgrid[l2y][l1x])
    # don't remove padding and splitting
    return(''.join(plain_text))

cipher_grid = make_cgrid(keyword)
plain_text = decrypt(input, cipher_grid)
print(plain_text)
