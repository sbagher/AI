# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 46, Chapter: 06, Book: "Practical Social Network Analysis with Python"

import networkx as nx
import numpy as np

print('Problem: 46, Chapter: 06, Book: "Practical Social Network Analysis with Python"\n')
print('Create random networks for α = 0.1, 0.2, ... , 10. For each of these networks,\n\
sample 1000 unique random (s, t) pairs (s != t). Then do a decentralized search\n\
starting from s as follows. Assuming that the current node is s, pick its neighbour\n\
u with smallest h(u, t) (break ties arbitrarily). If u = t, the search succeeds. If\n\
h(s, t) > h(u, t), set s to u and repeat. If h(s, t) ≤ h(u, t), the search fails.\n\n\
For each α, pick 1000 pairs of nodes and compute the average path length for the\n\
searches that succeeded. Then draw a plot of the average path length as a function\n\
of α. Also, plot the search success probability as a function of α.\n')

def h (v,u):
    t = 511
    for i in range(1,10,1):
        t = t<<1
        if (v & t)==(u & t):
            print (i)
            break

