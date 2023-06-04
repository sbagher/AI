# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 10, Chapter: 01, Book: "Practical Social Network Analysis with Python"

import networkx as nx
import random

# read the edges from the 'email-Eu-core.txt' file
G = nx.read_edgelist('email-Eu-core.txt', create_using=nx.DiGraph())

print('Problem: 10, Chapter: 01, Book: "Practical Social Network Analysis with Python"\n')
print('Distance between five pairs of random nodes')

nodes = list(G.nodes)
node_pairs = []
for i in range(5):
    pair = random.sample(nodes, 2)
    node_pairs.append(tuple(pair))

print("Nodes:\n\t", node_pairs)

for pair in node_pairs:
    source, target = pair
    try:
        distance = nx.shortest_path_length(G, source=source, target=target)
        print(f"Distance between nodes {source} and {target}: {distance}")
    except nx.NodeNotFound as e:
        print(f"Node not found: {e}")
    except nx.NetworkXNoPath as e:
        print(f"No path found: {e}")
