# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 35, Chapter: 04, Book: "Practical Social Network Analysis with Python"

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

print('Problem: 35, Chapter: 04, Book: "Practical Social Network Analysis with Python"\n')
print('Clustering coefﬁcient distributions\n')

# read the edges from the 'CA-AstroPh.txt' file
rwg = nx.read_edgelist('CA-GrQc.txt', create_using=nx.Graph(), comments='#')

rwg_nodes = len(rwg.nodes())

swg = nx.watts_strogatz_graph(rwg_nodes, 5, 0.5, seed=10)

plt.rcParams["figure.figsize"] = (15,5)
def show_dist(g,i,t):
    clustering_coeffs = nx.clustering(g)
    counter = {}
    for t1 in np.arange(0, 1.1, 0.1):
        counter[round(t1,1)] = 0

    for coeff in clustering_coeffs.values():
        c = round(coeff,1)
        counter[c] += 1

    plt.subplot(1, 2, i)
    plt.bar(np.arange(0, 1.1, 0.1), counter.values(), color ='green', width = 0.4)
    plt.title(f'Clustering Coefficient Distribution Histogram for \n{t}')
    plt.xlabel('Clustering Coefficient')
    plt.ylabel('Frequency')

show_dist(rwg,1,"Real World Graph")
show_dist(swg,2,"Small World Graph")
plt.show()