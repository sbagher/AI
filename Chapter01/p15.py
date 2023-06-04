# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 15, Chapter: 01, Book: "Practical Social Network Analysis with Python"

import networkx as nx

# read the edges from the 'email-Eu-core.txt' file
G = nx.read_edgelist('email-Eu-core.txt', create_using=nx.DiGraph())

print('Problem: 15, Chapter: 01, Book: "Practical Social Network Analysis with Python"\n')
print('Number of bridge edges')

G_undirected = G.to_undirected(as_view=True)
bridges = list(nx.bridges(G_undirected))
print(f"\nQ15: Number of bridge edges: {len(bridges)}")