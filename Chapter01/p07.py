# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 07, Chapter: 01, Book: "Practical Social Network Analysis with Python"

import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter

# read the edges from the 'email-Eu-core.txt' file
G = nx.read_edgelist('email-Eu-core.txt', create_using=nx.DiGraph())

print('Problem: 07, Chapter: 01, Book: "Practical Social Network Analysis with Python"\n')
print('In-degree distribution')

dgsq = [G.in_degree(n) for n in nx.nodes(G)]
freq=dict(Counter(dgsq))
print (sort(freq))
plt.hist(dgsq, bins=max(dgsq))
plt.title('In-Degree Histogram')
plt.xlabel('In-Degree')
plt.ylabel('Frequency')
plt.show()