# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 23, Chapter: 02, Book: "Practical Social Network Analysis with Python"

import networkx as nx
import random

# read the edges from the 'soc-Epinions1.txt' file
G = nx.read_edgelist('soc-Epinions1.txt', create_using=nx.DiGraph(), comments='#')

print('Problem: 23, Chapter: 02, Book: "Practical Social Network Analysis with Python"\n')
print('Choose 100 nodes at random from the network and do one forward and one\n\
backward BFS traversal for each node. Plot the cumulative distributions of the nodes\n\
covered in these BFS runs as shown in Fig. 2.7. Create one figure for the forward BFS\n\
and one for the backward BFS. Howmany nodes are in the OUT and IN components?\n\
How many nodes are in the TENDRILS component?\n')

random_nodes = random.sample(list(G.nodes()), 100)

for node in random_nodes:
    inv = list(nx.bfs_predecessors(G,node))

    outv = list(nx.bfs_successors(G,node))
    print(f"\tNumber of nodes in In({node}):\t{len(inv)} and in Out({node}):\t{len(outv)}")
