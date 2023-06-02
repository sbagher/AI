import networkx as nx

G = nx.read_edgelist('soc-Epinions1.txt', create_using=nx.DiGraph())

print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())

