# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 24, Chapter: 02, Book: "Practical Social Network Analysis with Python"

import networkx as nx
import random
import matplotlib.pyplot as plt
from collections import Counter

# read the edges from the 'soc-Epinions1.txt' file
G = nx.read_edgelist('soc-Epinions1.txt', create_using=nx.DiGraph(), comments='#')

print('Problem: 24, Chapter: 02, Book: "Practical Social Network Analysis with Python"\n')
print('What is the probability that a path exists between two nodes chosen uniformly \
from the graph? What if the node pairs are only drawn from the WCC of the two \
networks? Compute the percentage of node pairs that were connected in each of \
these cases.\n')

N = nx.DiGraph()
nx.add_path(N, [0, 1, 2, 3, 4, 7])
nx.add_path(N, [3, 5, 6, 7,9])
nx.add_path(N, [4, 9])
print(dict(nx.bfs_predecessors(N, source=0)))
print(dict(nx.bfs_successors(N, source=0)))
ps=list(nx.bfs_edges(N,9,True))
t=set()
for i,j in ps:
    t|={j}
print(t,len(t))