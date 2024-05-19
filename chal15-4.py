# change the first word to the second in as few steps as possible, changing
#  only one letter each time, to a valid word each change. Multiply the number
#  of words needed
import os
import numpy as np
import networkx as nx

wordfile = 'words.txt'
filename = 'input15.txt'
#filename = 'test15.txt'

# put words into numpy arrays by length, assuming nothing longer than 29
words_by_len = [[] for x in range(30)]
with open(wordfile) as f:
    words = f.read().strip().split('\n')
while len(words) > 0:
    word = words.pop()
    words_by_len[len(word)].append([ord(c) for c in word])

# now to numpy for each set >1, and into the network for those off by 1
g = nx.Graph()
for i in range(len(words_by_len)):
    num_words = len(words_by_len[i])
    if num_words > 1:
        print("Starting words of len", i, "of which there are", num_words)
        m = np.array(words_by_len[i], dtype=np.uint8)
        for j in range(m.shape[0]-1):
            diff_matrix = np.sum(m[j+1:] != m[j], axis=1)
            one_away = np.where((diff_matrix == 1) & \
                                (np.arange(num_words-(j+1)) != j))[0].tolist()
            # if anything is one char away, we should now have those
            a = tuple(m[j].tolist())
            for k in one_away:
                b = tuple(m[k+j+1].tolist())
                g.add_edge(a, b)
print("network created...")

with open(filename) as f:
    ls = f.read().strip().split('\n')
product_of_words = 1
for pair in ls:
    start, dest = pair.split(',')
    start = tuple([ord(c) for c in start])
    dest = tuple([ord(c) for c in dest])
    len_words = nx.dijkstra_path_length(g, source=start, target=dest) + 1
    product_of_words *= len_words

print("The product of word lengths is", product_of_words)
