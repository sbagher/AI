# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 52, Chapter: 08, Book: "Practical Social Network Analysis with Python"


import networkx as nx
import numpy as np

print('Problem: 52, Chapter: 08, Book: "Practical Social Network Analysis with Python"\n')
print('Perform these configurations and iterations, and compute who wins in the first\n\
graph, and by how much? Similarly, compute the votes for the second graph.')

g1 = nx.gnm_random_graph(10000, 100000, seed=10, directed=False)
g2 = nx.barabasi_albert_graph(10000,10,10)

def election(g):
    c0 = {8,9}
    c1 = {0,2,4,6}
    c2 = {1,3,5,7}
    for _ in range (10):
        for n in g.nodes():
            t = n % 10
            if t in c0:
                
            else:
                continue
