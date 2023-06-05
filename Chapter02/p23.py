# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 23, Chapter: 02, Book: "Practical Social Network Analysis with Python"

import networkx as nx
import random
import matplotlib.pyplot as plt
import numpy as np

# read the edges from the 'soc-Epinions1.txt' file
G = nx.read_edgelist('soc-Epinions1.txt', create_using=nx.DiGraph(), comments='#')

print('Problem: 23, Chapter: 02, Book: "Practical Social Network Analysis with Python"\n')
print('Choose 100 nodes at random from the network and do one forward and one\n\
backward BFS traversal for each node. Plot the cumulative distributions of the nodes\n\
covered in these BFS runs as shown in Fig. 2.7. Create one figure for the forward BFS\n\
and one for the backward BFS. Howmany nodes are in the OUT and IN components?\n\
How many nodes are in the TENDRILS component?\n')

random_nodes = random.sample(list(G.nodes()), 100)
bbfs = []
fbfs =  []

for node in random_nodes:
    bbfs.append(len(list(nx.bfs_predecessors(G,node))))
    fbfs.append(len(list(nx.bfs_successors(G,node))))

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(sorted(fbfs), color = 'blue')
plt.xscale('linear')
plt.yscale('log')
plt.xlabel('Percent of Starting Nodes')
plt.ylabel('Number of Nodes Reached')
plt.title('Forward BFS')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(sorted(bbfs), color = 'maroon')
plt.xscale('linear')
plt.yscale('log')
plt.xlabel('Percent of Starting Nodes')
plt.ylabel('Number of Nodes Reached')
plt.title('Backward BFS')
plt.grid(True)

plt.show()