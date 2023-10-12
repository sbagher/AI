# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 51, Chapter: 08, Book: "Practical Social Network Analysis with Python"


import networkx as nx
import numpy as np

print('Problem: 51, Chapter: 08, Book: "Practical Social Network Analysis with Python"\n')
print('A preferential attachment graph with 10000 nodes with out-degree 10.')

g2 = nx.barabasi_albert_graph(10000,10,10)
