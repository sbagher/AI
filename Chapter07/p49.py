# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 49, Chapter: 07, Book: "Practical Social Network Analysis with Python"


import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

print('Problem: 49, Chapter: 07, Book: "Practical Social Network Analysis with Python"\n')
print('Now, analyse a simple generative model of signed networks by running simulations\n\
of the dynamic process on small networks in the following manner. Create a\n\
complete network on 10 nodes. For each edge, choose a sign with uniform probability.\n\
Run this dynamic process for a million iterations. Repeat this process 100 times.\n\
What fraction of these networks are balanced?')

g = nx.complete_graph(10, nx.Graph())
g.remove_edges_from(nx.selfloop_edges(g))
ec = g.number_of_edges()
for _ in range(100):
    for p in np.random.uniform(0,1,1000000):
        s = np.random.uniform(0,1,ec) < p
