# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 25, Chapter: 03, Book: "Practical Social Network Analysis with Python"

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# read the edges from the 'CA-AstroPh.txt' file
rwg = nx.read_edgelist('CA-AstroPh.txt', create_using=nx.DiGraph(), comments='#')
rwg_nodes = len(rwg.nodes())
rwg_edges = len(rwg.edges())
ind = [rwg.in_degree(n) for n in nx.nodes(rwg)]
outd = [rwg.out_degree(n) for n in nx.nodes(rwg)]

rg = nx.gnm_random_graph(rwg_nodes,rwg_edges,seed=10,directed=True)

cg = nx.directed_configuration_model (ind,outd,seed=10)

dgsq = [G.degree(n) for n in nx.nodes(G)]
plt.hist(dgsq, bins=max(dgsq))
plt.title('In-Degree Histogram')
plt.xlabel('In-Degree')
plt.ylabel('Frequency')
plt.show()