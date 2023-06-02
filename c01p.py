import networkx as nx

# read the edges from the 'email-Eu-core.txt' file
G = nx.read_edgelist('email-Eu-core.txt', create_using=nx.DiGraph())

# Q1: Number of nodes
print('\nQ1: Number of nodes: ', len(G.nodes()))

# Q2: Number of edges
print('\nQ2: Number of edges:', len(G.edges()))

# Q3: In-degree, out-degree and degree of the first five nodes
print('\nQ3: In-degree, out-degree and degree of the first five nodes')
for n in list(G.nodes)[0:5]:
    print('node:', n, '{in-degree:', G.in_degree(n), 'out-degree:', G.out_degree(n), 'degree:', G.degree(n),"}")

# Q4: Number of source nodes
src = []
for n in G.nodes():
    if G.in_degree(n) == 0:
        src.append(n)
print('\nQ4: Number of source nodes: ', len(src))

# Q5: Number of sink nodes
snk = []
for n in G.nodes():
    if G.out_degree(n) == 0:
        snk.append(n)
print('\nQ5: Number of sink nodes: ', len(snk))

# Q6: Number of isolated nodes
isl = []
for n in G.nodes():
    if G.degree(n) == 0:
        isl.append(n)
print('\nQ6: Number of isolated nodes: ', len(isl))