# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 25, Chapter: 03, Book: "Practical Social Network Analysis with Python"

import snap

print('Problem: 25, Chapter: 03, Book: "Practical Social Network Analysis with Python"\n')
print('Erdös–Rényi random graph (G(n, m): Generate a random instance of this model by using the number of nodes and edges as the real world graph.\n')


rg2 = snap.GenRndGnm(snap.TNGraph, 18772,198110)
rg2.SaveEdgeList('Erdos–Renyi.txt')
