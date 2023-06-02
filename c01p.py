import networkx as nx

G = nx.read_edgelist('email-Eu-core.txt', create_using=nx.DiGraph())
