# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 10, Chapter: 01, Book: "Practical Social Network Analysis with Python"

import networkx as nx

# read the edges from the 'email-Eu-core.txt' file
G = nx.read_edgelist('email-Eu-core.txt', create_using=nx.DiGraph())

print('Problem: 10, Chapter: 01, Book: "Practical Social Network Analysis with Python"\n')
print('Distance between five pairs of random nodes')

print("\tAverage degree:", sum([G.degree(n) for n in nx.nodes(G)]) / len(G.nodes))
print("\tAverage in-degree:", sum([G.in_degree(n) for n in nx.nodes(G)]) / len(G.nodes))
print("\tAverage out-degree:", sum([G.out_degree(n) for n in nx.nodes(G)]) / len(G.nodes))