# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 29, Chapter: 03, Book: "Practical Social Network Analysis with Python"

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

print('Problem: 29, Chapter: 03, Book: "Practical Social Network Analysis with Python"\n')
print('Clustering coefﬁcient distributions\n')

# read the edges from the 'CA-AstroPh.txt' file
rwg = nx.read_edgelist('CA-AstroPh.txt', create_using=nx.DiGraph(), comments='#')

rwg_nodes = len(rwg.nodes())
rwg_edges = len(rwg.edges())
ind = [rwg.in_degree(n) for n in nx.nodes(rwg)]
outd = [rwg.out_degree(n) for n in nx.nodes(rwg)]

rg = nx.gnm_random_graph(rwg_nodes,rwg_edges,seed=10,directed=True)

cg = nx.directed_configuration_model (ind,outd,seed=10)
cg = nx.DiGraph(cg)

plt.rcParams["figure.figsize"] = (15,5)
def show_dist(g,i,t):
    clustering_coeffs = nx.clustering(g)
    counter = {}
    for t1 in np.arange(0, 1.1, 0.1):
        counter[round(t1,1)] = 0

    for coeff in clustering_coeffs.values():
        c = round(coeff,1)
        counter[c] += 1

    plt.subplot(1, 3, i)
    plt.bar(np.arange(0, 1.1, 0.1), counter.values(), color ='green', width = 0.4)
    plt.title(f'Clustering Coefficient Distribution Histogram for \n{t}')
    plt.xlabel('Clustering Coefficient')
    plt.ylabel('Frequency')
show_dist(rwg,1,"Real World Graph")
show_dist(rg,2,"Erdös–Rényi Random Graph")
show_dist(cg,3,"Conﬁguration Model Random Graph")
plt.show()