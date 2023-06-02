import networkx as nx

# read the edges from the 'email-Eu-core.txt' file
G = nx.read_edgelist('email-Eu-core.txt', create_using=nx.DiGraph())

# Q1: Number of nodes
print('\nQ1: Number of nodes: ', len(G.nodes()))

# Q2: Number of edges
print('\nQ2: Number of edges:', len(G.edges()))