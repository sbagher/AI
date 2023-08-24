# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 25, Chapter: 03, Book: "Practical Social Network Analysis with Python"

import networkx as nx

print('Problem: 25, Chapter: 03, Book: "Practical Social Network Analysis with Python"\n')
print('Erdös–Rényi random graph (G(n, m): Generate a random instance of this model by using the number of nodes and edges as the real world graph.\n')

# read the edges from the 'CA-AstroPh.txt' file
rwg = nx.read_edgelist('CA-AstroPh.txt', create_using=nx.Graph(), comments='#')

rwg_nodes = len(rwg.nodes())
rwg_edges = len(rwg.edges())

rg = nx.gnm_random_graph(rwg_nodes,rwg_edges,seed=10,directed=False)
