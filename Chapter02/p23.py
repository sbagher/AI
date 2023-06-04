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

random_nodes = random.sample(list(G.nodes()), 50)
inv, outv = [], []

for node in random_nodes:
    inv.append(len(list(nx.bfs_predecessors(G,node))))
    outv.append(len(list(nx.bfs_successors(G,node))))

def plot_BFS(covered_nodes,color,lable):
    max_covered_nodes = max(covered_nodes)
    freq=np.zeros(max_covered_nodes + 1)
    for covered_node in covered_nodes:
        freq[covered_node] += 1
    degree_prob=freq/sum(freq)
    # Plot the in-degree distribution
    plt.figure(figsize=(10, 5))
    plt.plot(degree_prob, range(len(degree_prob)), color)
    plt.xscale('linear')
    plt.yscale('log')
    plt.xlabel(f'{lable}-degree')
    plt.ylabel('Probability')
    plt.title(f'{lable}-degree Distribution')
    plt.grid(True)
    plt.show()

plot_BFS (inv,'bo','In')
plot_BFS (outv,'ro','Out')