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
# make a matrix to make looking up weights (dust) easier
m = []
for l in ls:
    m.append([-int(dust) for dust in l.split()])
# make the network using the left most column position in the label
g = nx.DiGraph()
for y, r in enumerate(m):
    if y == 0:
        continue
    for x in range(len(r) - (vac_width - 1)):
        if x == 0:
            w = sum(m[y-1][x:x+vac_width])
            g.add_edge(f"R{y-1}C{x}", f"R{y}C{x}", weight=w)
            w = sum(m[y-1][x+1:x+1+vac_width])
            g.add_edge(f"R{y-1}C{x+1}", f"R{y}C{x}", weight=w)
        elif x == len(r) - vac_width:
            w = sum(m[y-1][x-1:(x-1)+vac_width])
            g.add_edge(f"R{y-1}C{x-1}", f"R{y}C{x}", weight=w)
            w = sum(m[y-1][x:x+vac_width])
            g.add_edge(f"R{y-1}C{x}", f"R{y}C{x}", weight=w)
        else:
            w = sum(m[y-1][x-1:(x-1)+vac_width])
            g.add_edge(f"R{y-1}C{x-1}", f"R{y}C{x}", weight=w)
            w = sum(m[y-1][x:x+vac_width])
            g.add_edge(f"R{y-1}C{x}", f"R{y}C{x}", weight=w)
            w = sum(m[y-1][x+1:x+1+vac_width])
            g.add_edge(f"R{y-1}C{x+1}", f"R{y}C{x}", weight=w)
# finish with a last dummy edge to contain final weights
y = len(m)
for x in range(len(m[-1]) - (vac_width - 1)):
    w = sum(m[y-1][x:x+vac_width])
    g.add_edge(f"R{y-1}C{x}", f"R{y}C{x}", weight=w)

# find shortest (weights are negative, so most dust)
sources = []
destinations = []
most_dust = 0
end_row = len(m)
for x in range(len(m[0]) - (vac_width - 1)):
    sources.append(f"R0C{x}")
    destinations.append(f"R{end_row}C{x}")
for source in sources:
    for target in destinations:
        path_dust = nx.bellman_ford_path_length(g, source, target,
                                                weight='weight')
        if path_dust < most_dust:
            most_dust = path_dust
T1 = time.perf_counter()
print(f"Largest possible amount of dust collected is {-most_dust}")
print(f"Time taken was {T1 - T0} seconds")
