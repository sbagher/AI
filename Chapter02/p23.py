# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 23, Chapter: 02, Book: "Practical Social Network Analysis with Python"

import networkx as nx
import random
import matplotlib.pyplot as plt
from collections import Counter

# read the edges from the 'soc-Epinions1.txt' file
G = nx.read_edgelist('soc-Epinions1.txt', create_using=nx.DiGraph(), comments='#')

print('Problem: 23, Chapter: 02, Book: "Practical Social Network Analysis with Python"\n')
print('Choose 100 nodes at random from the network and do one forward and one\n\
backward BFS traversal for each node. Plot the cumulative distributions of the nodes\n\
covered in these BFS runs as shown in Fig. 2.7. Create one figure for the forward BFS\n\
and one for the backward BFS. How many nodes are in the OUT and IN components?\n\
How many nodes are in the TENDRILS component?\n')

random_nodes = random.sample(list(G.nodes()), 100)
bbfs, fbfs = [], []
scc_set = set()
nodes_out = set()
nodes_in = set()

sccs = list(nx.strongly_connected_components(G))
max_scc_len=0
for scc in sccs:
    if len(scc)>max_scc_len:
        scc_set = scc
        max_scc_len=len(scc)

for node in random_nodes:
    bbfs_set = set(dict(nx.bfs_predecessors(G,node)).keys())
    bbfs_set -= {node}
    bbfs.append(len(bbfs_set))
    fbfs_set = set(dict(nx.bfs_successors(G,node)).keys())
    fbfs_set -= {node}
    fbfs.append(len(fbfs_set))
    nodes_out |= fbfs_set
    nodes_in |= bbfs_set

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(sorted(fbfs), color = 'blue')
plt.xscale('linear')
plt.yscale('log')
plt.xlabel('Frac. (in percent) of Starting Nodes')
plt.ylabel('Number of Nodes Reached')
plt.title('Forward BFS')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(sorted(bbfs), color = 'maroon')
plt.xscale('linear')
plt.yscale('log')
plt.xlabel('Frac. (in percent) of Starting Nodes')
plt.ylabel('Number of Nodes Reached')
plt.title('Backward BFS')
plt.grid(True)

plt.show()

nodes_out -= scc_set
nodes_in -= scc_set

print("Nodes in biggest SCC component:", len(scc_set))
print("Nodes in OUT component:", len(nodes_out))
print("Nodes in IN component:", len(nodes_in))
print("Nodes in TENDRILS component:", len(G.nodes())-len(scc_set)-len(nodes_out)-len(nodes_in))