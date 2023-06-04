# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 01, Chapter: 01, Book: "Practical Social Network Analysis with Python"

import networkx as nx

# read the edges from the 'email-Eu-core.txt' file
G = nx.read_edgelist('email-Eu-core.txt', create_using=nx.DiGraph())

# P01: Number of nodes
print('Problem: 01, Chapter: 01, Book: "Practical Social Network Analysis with Python"\n')
print('Number of nodes:', len(G.nodes()))