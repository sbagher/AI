# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 19, Chapter: 01, Book: "Practical Social Network Analysis with Python"

import networkx as nx
import random

# read the edges from the 'email-Eu-core.txt' file
G = nx.read_edgelist('email-Eu-core.txt', create_using=nx.DiGraph())

print('Problem: 19, Chapter: 01, Book: "Practical Social Network Analysis with Python"\n')
print('Clustering coefficient for five random nodes')

random_nodes = random.sample(list(G.nodes()), 5)

for node in random_nodes:
    print(f"\tClustering coefficient of node {node}: {nx.clustering(G, node)}")
