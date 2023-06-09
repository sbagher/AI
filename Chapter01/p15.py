# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 15, Chapter: 01, Book: "Practical Social Network Analysis with Python"

import networkx as nx

# read the edges from the 'email-Eu-core.txt' file
G = nx.read_edgelist('email-Eu-core.txt', create_using=nx.DiGraph())

print('Problem: 15, Chapter: 01, Book: "Practical Social Network Analysis with Python"\n')

# Algorithm #1
UG = G.to_undirected()
bridges = list(nx.bridges(UG))
print(f"First Algorithm (Fast): Convert to undirected graph and use bridges() function)")
print(f"\tNumber of bridge edges: {len(bridges)}")

# Algorithm #2
# create weakly connected components
print(f"Second Algorithm (Slow, Please waite ...): Remove each edge and check if the number of weakly connected graph is changed?")

nwccs = len(list(nx.weakly_connected_components(G)))
num_bridge_edges = 0
edges = list(G.edges())

# iterate over edges and check if they are bridge edges
for u, v in edges:
    # remove edge (u, v) from the graph
    G.remove_edge(u, v)
    
    # check if the number of weakly connected graph is changed?
    if len(list(nx.weakly_connected_components(G))) != nwccs:
        num_bridge_edges += 1
    
    # add edge (u, v) back to the graph
    G.add_edge(u, v)
# print the number of bridge edges
print(f"\tNumber of bridge edges: {num_bridge_edges}")
