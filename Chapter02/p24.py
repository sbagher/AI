# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 23, Chapter: 02, Book: "Practical Social Network Analysis with Python"

import networkx as nx

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