# change the first word to the second in as few steps as possible, changing
#  only one letter each time, to a valid word each change. Multiply the number
#  of words needed
import networkx as nx

wordfile = 'words.txt'
filename = 'input15.txt'
#filename = 'test15.txt'

def offByOne(w1, w2):
    '''Test if the two words differ by a single letter and return True if
    they do and false otherwise'''
    if len(w1) != len(w2):
        return(False)
    diffs = 0
    for i, c in enumerate(w1):
        if c != w2[i]:
            diffs += 1
            if diffs > 1:
                return(False)
    return(True)

# let's make a network of words that are 1 letter apart. Then a shortest
#  path should tell us the minimum words between the start and finish
g = nx.Graph()
with open(wordfile) as f:
    words = f.read().strip().split('\n')
print(f'Our word list is {len(words)} long')
while len(words) > 0:
    word = words.pop()
    if len(words) % 1000 == 0:
        print(len(words), "words left")
    for compare_word in words:
        if offByOne(word, compare_word):
            g.add_edge(word, compare_word)
print("network created...")

with open(filename) as f:
    ls = f.read().strip().split('\n')

product_of_words = 1
for pair in ls:
    start, dest = pair.split(',')
    len_words = nx.dijkstra_path_length(g, source=start, target=dest) + 1
    product_of_words *= len_words

print("The product of word lengths is", product_of_words)
