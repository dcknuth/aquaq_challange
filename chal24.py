# build a Huffman encoding tree with the first part of the input.
#  then decode the message in the second part
from operator import itemgetter

DEBUG = 4
filename = 'input24.txt'
#filename = 'test24.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

# let's make an object for this since I don't know of a nice tree module
class HuffTree:
    def __init__(self, r=None, l=None, parent=None, name='', weight=0):
        if r == None and name == '':
            print("Error: need an r and l or a name")
            return(None)
        if r == None:
            self.name = name
            self.weight = weight
        else:
            self.name = l.name + r.name
            self.weight = l.weight + r.weight
            l.parent = self
            r.parent = self
        self.l = l
        self.r = r
    
    def __str__(self):
        return(f"{self.name}:{self.weight}")


# make our Huffman tree
construct = ls[0]
# get a frequency count
letters = set(construct)
l_counts = dict()
for l in letters:
    l_counts[l] = construct.count(l)
# make a list sorted by count and then ASCII val
count_list = list(l_counts.items())
# need to do ASCII first (default for sort)
count_list.sort()
# then count
count_list.sort(key=itemgetter(1))
# convert the list to tree nodes
nodes = []
for i in count_list:
    nodes.append(HuffTree(name=i[0], weight=i[1]))
# build the tree
while len(nodes) > 1:
    n1 = nodes.pop(0)
    n2 = nodes.pop(0)
    cur_tree = HuffTree(r=n2, l=n1)
    # insert in the right spot
    if len(nodes) == 0:
        nodes.append(cur_tree)
    else:
        pos = 0
        for i in range(len(nodes)):
            if cur_tree.weight < nodes[i].weight:
                pos = i
                break
            elif cur_tree.weight == nodes[i].weight and \
                len(cur_tree.name) < len(nodes[i].name):
                pos = i
                break
            elif cur_tree.weight == nodes[i].weight and \
                len(cur_tree.name) < len(nodes[i].name) and \
                cur_tree.name < nodes[i].name:
                pos = i
                break
            else:
                pos = i+1
        nodes.insert(pos, cur_tree)
huff_tree = nodes.pop()
# did this work
if(DEBUG > 4):
    print_line = [huff_tree]
    while len(print_line) > 0:
        new_line = []
        for l in print_line:
            print(l)
            if l.l != None:
                new_line.append(l.l)
            if l.r != None:
                new_line.append(l.r)
        print_line = new_line

# now we should be able to create the binary dictionary
c_to_b = dict()
for l in letters:
    lr_list = []
    cur_node = huff_tree
    while cur_node.name != l:
        if l in cur_node.l.name:
            lr_list.append('0')
            cur_node = cur_node.l
        else:
            lr_list.append('1')
            cur_node = cur_node.r
    c_to_b[l] = ''.join(lr_list)
# and get the reverse lookup
b_to_c = {value:key for key, value in c_to_b.items()}

# now to finally decompress the compressed message
compressed = list(ls[1])
decompressed = []
while len(compressed) > 0:
    b_str = compressed.pop(0)
    while b_str not in b_to_c:
        b_str = b_str + compressed.pop(0)
    decompressed.append(b_to_c[b_str])

print(''.join(decompressed))
