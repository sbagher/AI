# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 03, Chapter: 01, Book: "Practical Social Network Analysis with Python"

import networkx as nx

# read the edges from the 'email-Eu-core.txt' file
G = nx.read_edgelist('email-Eu-core.txt', create_using=nx.DiGraph())

print('\nProblem: 03, Chapter: 01, Book: "Practical Social Network Analysis with Python"\n')
print('\nIn-degree, out-degree and degree of the first five nodes')

for n in list(G.nodes)[0:5]:
    print('\tnode:', n, '{in-degree:', G.in_degree(n), 'out-degree:', G.out_degree(n), 'degree:', G.degree(n),"}")