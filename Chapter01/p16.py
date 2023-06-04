# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 16, Chapter: 01, Book: "Practical Social Network Analysis with Python"

import networkx as nx

# read the edges from the 'email-Eu-core.txt' file
G = nx.read_edgelist('email-Eu-core.txt', create_using=nx.DiGraph())

print('Problem: 16, Chapter: 01, Book: "Practical Social Network Analysis with Python"\n')

# Algorithm #1
UG = G.to_undirected()
articulation_nodes = list(nx.articulation_points(UG))
print(f"First Algorithm (Fast): Convert to undirected graph and use articulation_points() function)")
print(f"\tNumber of articulation nodes: {len(articulation_nodes)}")

# Algorithm #2
# create weakly connected components
print(f"Second Algorithm (Slow, Please waite...): Remove each node and check: is the new graph connected too?")

nwccs = len(list(nx.weakly_connected_components(G)))
num_articulation_nodes = 0
nodes = list(G.nodes())

# iterate over nodes and check if they are articulation nodes
for n in nodes:
    GT=G.copy()
    GT.remove_node(n)
    
    # check if the graph is still weakly connected
    if len(list(nx.weakly_connected_components(GT))) != nwccs:
        num_articulation_nodes += 1
    
# print the number of bridge edges
print(f"\tNumber of bridge edges: {num_articulation_nodes}")
