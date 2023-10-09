# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 48, Chapter: 07, Book: "Practical Social Network Analysis with Python"


import networkx as nx
import matplotlib.pyplot as plt

print('Problem: 48, Chapter: 07, Book: "Practical Social Network Analysis with Python"\n')
print('Calculate the fraction of positive and negative edges in the graph. Let the fraction\n\
of positive edges be p. Assuming that each edge of a triad will independently be.\n\
assigned a positive sign with probability p and a negative sign with probability\n\
1 − p, calculate the probability of each type of triad.\n')

# read the edges from the 'soc-sign-epinions.txt' file
g = nx.read_edgelist('soc-sign-epinions.txt', create_using=nx.MultiGraph(), comments='#', nodetype=int, data=(("sign", int),))
g.remove_edges_from(nx.selfloop_edges(g))

p, n = 0, 0
for u, v, keys, sign in g.edges(data="sign", keys=True):
    if sign == 1:
        p += 1
    else:
        n += 1

t = p + n
p, n = p/t, n/t
print (f"fraction of positive edges:{p}")
print (f"fraction of negative edges:{n}")

