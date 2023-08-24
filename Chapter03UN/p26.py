# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 26, Chapter: 03, Book: "Practical Social Network Analysis with Python"

import networkx as nx

print('Problem: 26, Chapter: 03, Book: "Practical Social Network Analysis with Python"\n')
print('Conﬁguration model random graph: Generate a random instance of this model by using the graph in the dataset\n')

# read the edges from the 'CA-AstroPh.txt' file
rwg = nx.read_edgelist('CA-AstroPh.txt', create_using=nx.Graph(), comments='#')

d = [rwg.degree(n) for n in nx.nodes(rwg)]

cg = nx.configuration_model (d,seed=10)