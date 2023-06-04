# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 17, Chapter: 01, Book: "Practical Social Network Analysis with Python"

import networkx as nx
import random

# read the edges from the 'email-Eu-core.txt' file
G = nx.read_edgelist('email-Eu-core.txt', create_using=nx.DiGraph())

print('Problem: 17, Chapter: 01, Book: "Practical Social Network Analysis with Python"\n')

# Q17: Number of nodes in In(v) for five random nodes
print('\nQ17: Number of nodes in In(v) for five random nodes')
random_nodes = random.sample(list(G.nodes()), 5)

for node in random_nodes:
    in_neighbors = list(G.predecessors(node))
    print(f"\tNumber of nodes in In({node}): {len(list(in_neighbors))}")
    print (in_neighbors)
