# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 05, Chapter: 01, Book: "Practical Social Network Analysis with Python"

import networkx as nx

# read the edges from the 'email-Eu-core.txt' file
G = nx.read_edgelist('email-Eu-core.txt', create_using=nx.DiGraph())

print('Problem: 05, Chapter: 01, Book: "Practical Social Network Analysis with Python"\n')

src = [n for n in G.nodes() if G.out_degree(n) == 0]
print('Number of sink nodes:', len(src))