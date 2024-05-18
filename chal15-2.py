# change the first word to the second in as few steps as possible, changing
#  only one letter each time, to a valid word each change. Multiply the number
#  of words needed
import networkx as nx

wordfile = 'words.txt'
filename = 'input15.txt'
#filename = 'test15.txt'

def offByOne(w1, w2):
    '''Test if the two words differ by a single letter and return True if
    they do and false otherwise. This will only get words of the same length
    so no need to test for that anymore'''
    diffs = 0
    for i, c in enumerate(w1):
        if c != w2[i]:
            diffs += 1
            if diffs > 1:
                return(False)
    return(True)

# put words into lists by length, assuming nothing longer than 29
words_by_len = [[] for x in range(30)]
with open(wordfile) as f:
    words = f.read().strip().split('\n')
while len(words) > 0:
    word = words.pop()
    words_by_len[len(word)].append(word)
for i in range(len(words_by_len)):
    print('Word list for length', i, 'is', len(words_by_len[i]), 'long')

# let's make a network of words that are 1 letter apart. Then a shortest
#  path should tell us the minimum words between the start and finish
g = nx.Graph()
# add to graph in groups by length of the words
for i in range(len(words_by_len)):
    while len(words_by_len[i]) > 0:
        word = words_by_len[i].pop()
        for compare_word in words_by_len[i]:
            if offByOne(word, compare_word):
                g.add_edge(word, compare_word)
    print("Words of length", i, "added")
print("network created...")

with open(filename) as f:
    ls = f.read().strip().split('\n')
product_of_words = 1
for pair in ls:
    start, dest = pair.split(',')
    len_words = nx.dijkstra_path_length(g, source=start, target=dest) + 1
    product_of_words *= len_words

print("The product of word lengths is", product_of_words)
