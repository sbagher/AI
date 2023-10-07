# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 47, Chapter: 07, Book: "Practical Social Network Analysis with Python"


import networkx as nx
import matplotlib.pyplot as plt

print('Problem: 47, Chapter: 07, Book: "Practical Social Network Analysis with Python"\n')
print('Calculate the count and fraction of triads of each type in this network.\n')

# read the edges from the 'soc-sign-epinions.txt' file
g = nx.read_edgelist('soc-sign-epinions.txt', create_using=nx.Graph(), comments='#', nodetype=int, data=(("sign", int),))

for a, b in g.edges():
    print (a,b,g[a][b]['sign'])