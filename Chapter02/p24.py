# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 24, Chapter: 02, Book: "Practical Social Network Analysis with Python"

import networkx as nx
import random
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

print('Problem: 24, Chapter: 02, Book: "Practical Social Network Analysis with Python"\n')
print('What is the probability that a path exists between two nodes chosen uniformly \
from the graph? What if the node pairs are only drawn from the WCC of the two \
networks? Compute the percentage of node pairs that were connected in each of \
these cases.\n')

# read the edges from the 'soc-Epinions1.txt' file
g = nx.read_edgelist('soc-Epinions1.txt', create_using=nx.DiGraph(), comments='#')
g.remove_edges_from(nx.selfloop_edges(g))
g.remove_nodes_from(nx.isolates(g))

sccs = list(nx.strongly_connected_components(g))
sccs_len = [(len(scc), next(iter(scc))) for scc in sccs]
sccs = sorted (sccs_len, key=lambda x: x[0], reverse=True)

sccs_len = len(sccs)
shape = (sccs_len, sccs_len)
hp = np.zeros(shape, dtype=int)

cc = 0
ss = 0
for i in range(sccs_len):
    l1, n1 = sccs[i]
    c = 0
    s = 0
    for j in range(i):
        l2, n2 = sccs[j]
        if nx.has_path(g,n1,n2):
            s += l2
            c += 1
            hp[i][j] = 1
            for k in range(j+1,sccs_len):
                if hp[j][k] == 1:
                    hp[i][k] = 1

    if l1 != 1:
        s += (l1-1)
        c += 1
        hp[i][i] = 1
    
    for j in range(i+1,sccs_len):
        l2, n2 = sccs[j]
        if hp[i][j] == 1:
            s += l2
            c += 1
        else:
            if nx.has_path(g,n1,n2):
                s += l2
                c += 1
                hp[i][j] = 1
    if c != 0:
        ss += (l1*s)
        cc += 1

    nn = nx.number_of_nodes(g)
print (f'Probability that a path exists between two nodes: {ss/(nn*(nn-1))}')
print (f'Probability that a path exists between two nodes from the WCC of the two networks: {0}')