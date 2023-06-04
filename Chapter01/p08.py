# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 08, Chapter: 01, Book: "Practical Social Network Analysis with Python"

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# read the edges from the 'email-Eu-core.txt' file
G = nx.read_edgelist('email-Eu-core.txt', create_using=nx.DiGraph())

print('Problem: 08, Chapter: 01, Book: "Practical Social Network Analysis with Python"\n')
print('Out-degree distribution')

dgsq = [G.out_degree(n) for n in nx.nodes(G)]
plt.hist(dgsq, bins=max(dgsq))
plt.title('Out-Degree Histogram')
plt.xlabel('Out-Degree')
plt.ylabel('Frequency')
plt.show()

freq=np.zeros(max(dgsq) + 1)
for d in dgsq:
    freq[d] += 1
degree_prob=freq/sum(freq)
plt.bar(range(0,max(dgsq)+1),degree_prob,color ='maroon')
plt.title('Out-Degree distribution Histogram')
plt.xlabel('Out-Degree')
plt.ylabel('Probability')
plt.show()
