# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 20, Chapter: 01, Book: "Practical Social Network Analysis with Python"

import networkx as nx
import matplotlib.pyplot as plt

# read the edges from the 'email-Eu-core.txt' file
G = nx.read_edgelist('email-Eu-core.txt', create_using=nx.DiGraph())

print('Problem: 20, Chapter: 01, Book: "Practical Social Network Analysis with Python"\n')
print('Clustering coefficient distribution')

clustering_coeffs = nx.clustering(G)
counter = {}

for coeff in clustering_coeffs.values():
    if coeff in counter.keys():
        counter[coeff]  += 1
    else:
        counter[coeff] = 1

plt.hist(list(clustering_coeffs.values()), bins=max(list(counter.values())))
plt.title('Clustering coefficient distribution')
plt.xlabel('Clustering coefficient')
plt.ylabel('Frequency')
plt.show()

for coeff, freq in sorted(counter.items()):
    print(f"\t{coeff}:\t{freq}")