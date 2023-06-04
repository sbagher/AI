# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 14, Chapter: 01, Book: "Practical Social Network Analysis with Python"

import networkx as nx
from collections import Counter

# read the edges from the 'email-Eu-core.txt' file
G = nx.read_edgelist('email-Eu-core.txt', create_using=nx.DiGraph())

print('Problem: 14, Chapter: 01, Book: "Practical Social Network Analysis with Python"\n')
print('Is the graph weakly connected? If so, compute the weakly connected component size distribution')

if nx.is_weakly_connected(G):
    print("The graph is weakly connected.")
else:
    wccs = list(nx.weakly_connected_components(G))

    wcc_sizes = [len(wcc) for wcc in wccs]
    wcc_size_counts = Counter(wcc_sizes)

    print("The graph is not weakly connected. Weakly connected component size distribution:")
    for size, count in sorted(wcc_size_counts.items()):
        print(f"\t{size}: {count}")
print ("")
n=G.nodes('808')
