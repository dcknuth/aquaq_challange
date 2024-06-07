# Clean the most dust in one pass
import networkx as nx
import time

filename = 'input21.txt'
#filename = 'test21.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

vac_width = 5
#vac_width = 3

T0 = time.perf_counter()
# make a matrix with the original dust amounts
m = [[int(dust) for dust in l.split()] for l in ls]
# make a matrix to set up low weights for more dust
mw = []
for l in ls:
    mw.append([100 - int(dust) for dust in l.split()])
# make the network using the left most column position in the label
g = nx.DiGraph()
for y, r in enumerate(mw):
    if y == 0:
        continue
    for x in range(len(r) - (vac_width - 1)):
        d2 = sum(m[y][x:x+vac_width])
        if x == 0:
            d1 = sum(m[y-1][x:x+vac_width])
            w = sum(mw[y-1][x:x+vac_width])
            g.add_edge(f"R{y-1}C{x}D{d1}", f"R{y}C{x}D{d2}", weight=w)
            d1 = sum(m[y-1][x+1:x+1+vac_width])
            w = sum(mw[y-1][x+1:x+1+vac_width])
            g.add_edge(f"R{y-1}C{x+1}D{d1}", f"R{y}C{x}D{d2}", weight=w)
        elif x == len(r) - vac_width:
            d1 = sum(m[y-1][x-1:(x-1)+vac_width])
            w = sum(mw[y-1][x-1:(x-1)+vac_width])
            g.add_edge(f"R{y-1}C{x-1}D{d1}", f"R{y}C{x}D{d2}", weight=w)
            d1 = sum(m[y-1][x:x+vac_width])
            w = sum(mw[y-1][x:x+vac_width])
            g.add_edge(f"R{y-1}C{x}D{d1}", f"R{y}C{x}D{d2}", weight=w)
        else:
            d1 = sum(m[y-1][x-1:(x-1)+vac_width])
            w = sum(mw[y-1][x-1:(x-1)+vac_width])
            g.add_edge(f"R{y-1}C{x-1}D{d1}", f"R{y}C{x}D{d2}", weight=w)
            d1 = sum(m[y-1][x:x+vac_width])
            w = sum(mw[y-1][x:x+vac_width])
            g.add_edge(f"R{y-1}C{x}D{d1}", f"R{y}C{x}D{d2}", weight=w)
            d1 = sum(m[y-1][x+1:x+1+vac_width])
            w = sum(mw[y-1][x+1:x+1+vac_width])
            g.add_edge(f"R{y-1}C{x+1}D{d1}", f"R{y}C{x}D{d2}", weight=w)
# finish with a last dummy edge to contain final weights
y = len(m)
for x in range(len(m[-1]) - (vac_width - 1)):
    d1 = sum(m[y-1][x:x+vac_width])
    w = sum(mw[y-1][x:x+vac_width])
    g.add_edge(f"R{y-1}C{x}D{d1}", f"R{y}C{x}", weight=w)

# find shortest
sources = []
destinations = []
min_cost = 1000000
best_path = []
end_row = len(m)
for x in range(len(m[0]) - (vac_width - 1)):
    d1 = sum(m[0][x:x+vac_width])
    sources.append(f"R0C{x}D{d1}")
    destinations.append(f"R{end_row}C{x}")
for target in destinations:
    path_cost, path = nx.multi_source_dijkstra(g, sources, target,
                                            weight='weight')
    if min_cost > path_cost:
        min_cost = path_cost
        best_path = path

# Count the dust amount from the path node names
most_dust = 0
for node in best_path[:-1]:
    _, dust = node.split('D')
    most_dust += int(dust)
T1 = time.perf_counter()
print(f"Largest possible amount of dust collected is {most_dust}")
print(f"Time taken was {T1 - T0} seconds")
