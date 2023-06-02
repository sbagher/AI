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
    print('node:', n, 'in-degree:', G.in_degree(n), 'out-degree:', G.out_degree(n), 'degree:', G.degree(n))