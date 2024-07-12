# decipher the column scrambled message
TEST_MESSAGE = 'WE ARE DISCOVERED FLEE AT ONCE'
TESTING = False
filename = 'input35.txt'
if TESTING:
    filename = 'test35.txt'

with open(filename) as f:
    ls = f.read()
# need to remove the last carriage return
ls = ls[:-1]

def decode(encrypted, ordering):
    '''This function will use a single ordering instead of a word. This
    should let us cache and avoid other words that come out the same'''
    # first back to lines. To do this we divide the total message length
    #  by the order length we are trying to use
    length = len(encrypted) // len(ordering)
    cipher_text1 = []
    i = 0
    while i < len(encrypted):
        l = [c for c in encrypted[i:i+length]]
        cipher_text1.append(l)
        i += length
    # next we need to take rows and put them in the columns they were
    #  originally in
    # make a holding space
    cipher_text2 = []
    for i in range(len(encrypted) // len(cipher_text1)):
        l = [' ' for j in range(len(ordering))]
        cipher_text2.append(l)
    # fill the holding space
    for row_source in range(len(ordering)):
        col_target = ordering.index(row_source)
        for row_target, c in enumerate(cipher_text1[row_source]):
            cipher_text2[row_target][col_target] = c
    text = ''
    for row in cipher_text2:
        text = text + ''.join(row)
    return(text)

def produce_order(keyword):
    sorted_keyword = sorted(keyword)
    order = [0 for c in keyword]
    last_letter = ''
    last_key_position = -1
    for i, c in enumerate(sorted_keyword):
        if last_letter == c:
            j = keyword.index(c, last_key_position + 1)
        else:
            j = keyword.index(c)
        order[j] = i
        last_letter = c
        last_key_position = j
    return(tuple(order))

if TESTING:
    keyword = 'GLASS'
    # keyword = 'LEVER'
    order = produce_order(keyword)
    decoded = decode(ls, order)
    print(decoded)


# We will try to use the word list for both keys and seeing if the message
#  is now clear
with open('words.txt') as f:
    words = f.read().strip().split('\n')
# change to a dictionary for fast lookup
words = {word:True for word in words}

# strip the trailing hash
if not TESTING:
    ls = ls[:-1]
orders_used = dict()
for word in words:
    # word must be a multiple of the encrypted length, so skip those
    if len(ls) % len(word) != 0:
        continue
    order = produce_order(word)
    if order in orders_used:
        continue
    clear_text = decode(ls, order)
    clear_words = clear_text.split()
    recognized = 0
    for cw in clear_words[:6]:
        if cw.lower() in words:
            recognized += 1
    if recognized > 5:
        print('Clear text found and is:')
        print(clear_text)
        print("Key word is", word)
        break
