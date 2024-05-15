# how much to give Diddy fiddy
import networkx as nx
import matplotlib.pyplot as plt

filename = 'input10.txt'
#filename = 'test10.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

print(ls)

g = nx.Graph()
for l in ls[1:]:
    n1, n2, cost = l.split(',')
    cost = float(cost)
    g.add_edge(n1, n2, weight=cost)

# pos = nx.spring_layout(g)
# nx.draw(g, pos, with_labels=True, node_color='lightblue',
#         node_size=500)
# edge_labels = nx.get_edge_attributes(g, 'weight')
# nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels)
# plt.show()

cost = nx.dijkstra_path_length(g, source='TUPAC', target='DIDDY',
                               weight='weight')
print("Cost to get Diddy his fiddy is", cost)
