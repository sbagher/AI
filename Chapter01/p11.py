# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 11, Chapter: 01, Book: "Practical Social Network Analysis with Python"

import networkx as nx
from collections import Counter

# read the edges from the 'email-Eu-core.txt' file
G = nx.read_edgelist('email-Eu-core.txt', create_using=nx.DiGraph())

print('Problem: 11, Chapter: 01, Book: "Practical Social Network Analysis with Python"\n')
print('Shortest path length distribution')

path_lengths = []
for n in G.nodes:
    lengths = nx.shortest_path_length(G, n)
    path_lengths += list(lengths.values())

path_length_counts = Counter(path_lengths)
for length, count in sorted(path_length_counts.items()):
    print(f"\t{length}: {count}")
