# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 20, Chapter: 01, Book: "Practical Social Network Analysis with Python"

import networkx as nx
import random

# read the edges from the 'email-Eu-core.txt' file
G = nx.read_edgelist('email-Eu-core.txt', create_using=nx.DiGraph())

print('Problem: 20, Chapter: 01, Book: "Practical Social Network Analysis with Python"\n')
print('\nClustering coefficient distribution')

clustering_coeffs = nx.clustering(G)

for node, coeff in clustering_coeffs.items():
        print(f"\t{node}: {coeff}")