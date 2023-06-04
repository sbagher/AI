# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 12, Chapter: 01, Book: "Practical Social Network Analysis with Python"

import networkx as nx
from collections import Counter

# read the edges from the 'email-Eu-core.txt' file
G = nx.read_edgelist('email-Eu-core.txt', create_using=nx.DiGraph())

print('Problem: 12, Chapter: 01, Book: "Practical Social Network Analysis with Python"\n')

diameter=0
for n in G.nodes:
    lengths = nx.shortest_path_length(G, n)
    m=max(lengths.values())
    if m>diameter:
        diameter=m
print('Diameter is',diameter)
