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

if nx.is_strongly_connected(G):
    print("The graph is strongly connected.")
else:
    sccs = list(nx.strongly_connected_components(G))

    scc_sizes = [len(scc) for scc in sccs]
    scc_size_counts = Counter(scc_sizes)

    print("The graph is not strongly connected. Strongly connected component size distribution:")
    for size, count in sorted(scc_size_counts.items()):
        print(f"\t{size}: {count}")
