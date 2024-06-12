# find the words, sum letter values (a=1, b=2 ...) for each word, multiply
#  by word length and sum that
import networkx as nx
filename = 'input27.txt'
#filename = 'test27.txt'

with open(filename) as f:
    ls = f.read().split('\n')
# drop last blank row
ls = ls[:-1]

# make our network
g = nx.Graph()
for y in range(len(ls)):
    for x in range(len(ls[y])):
        if ls[y][x] != ' ':
            if y > 0:
                if ls[y-1][x] != ' ':
                    g.add_edge((y, x), (y-1, x))
            if y < len(ls) - 1:
                if ls[y+1][x] != ' ':
                    g.add_edge((y, x), (y+1, x))
            if x > 0:
                if ls[y][x-1] != ' ':
                    g.add_edge((y, x), (y, x-1))
            if x < len(ls[y]) -1:
                if ls[y][x+1] != ' ':
                    g.add_edge((y, x), (y, x+1))
            g.nodes[(y, x)]['letter'] = ls[y][x]

# the snake will start and end with only 1 edge for those nodes
degrees = g.degree()
st = []
for node, degree in degrees:
    if degree == 1:
        st.append(node)

# get the path of each of our snakes
paths = []
while len(st) > 0:
    cur_start = st.pop()
    x = 0
    for i, target in enumerate(st):
        if nx.has_path(g, cur_start, target):
            x = i
            paths.append(nx.shortest_path(g, cur_start, target))
            break
    st.pop(x)

# traverse the paths while calculating our answer
total = 0
for path in paths:
    cur_node = 0
    cur_values = []
    horizontal = False
    while cur_node < len(path):
        cur_val = ord(g.nodes[path[cur_node]]['letter'])
        cur_val -= ord('a') - 1
        cur_values.append(cur_val)
        cur_node += 1
        if cur_node < len(path) and cur_node == 1:
            # first set of horizontal
            if path[0][0] == path[cur_node][0]:
                horizontal = True
        elif cur_node < len(path):
            if horizontal and path[cur_node-1][0] != path[cur_node][0]:
                total += len(cur_values) * sum(cur_values)
                cur_values = []
                cur_values.append(cur_val)
                horizontal = not horizontal
            if not horizontal and path[cur_node-1][1] != path[cur_node][1]:
                total += len(cur_values) * sum(cur_values)
                cur_values = []
                cur_values.append(cur_val)
                horizontal = not horizontal
    # add value of final word
    total += len(cur_values) * sum(cur_values)

print("Sum of word values for all paths is", total)
