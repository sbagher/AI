# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 42, Chapter: 05, Book: "Practical Social Network Analysis with Python"

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

print('Problem: 42, Chapter: 05, Book: "Practical Social Network Analysis with Python"\n')
print('Clustering coefﬁcient distributions\n')

# Read the edges from the 'ca-HepPh.txt' instead of 'com-friendster.ungraph.txt' file,
# because friendster dataset needs huge memory and computing. Two mentioned files have 
# same characteristics (see https://snap.stanford.edu/data/index.html part "Networks with ground-truth communities")
# It seems that friendster dataset needs GraphX on Hadoop or Spark. So it can not run on my laptop!
rwg = nx.read_edgelist('ca-HepPh.txt', create_using=nx.DiGraph(), comments='#')

plt.rcParams["figure.figsize"] = (10,5)
def show_dist(g,i,t):
    clustering_coeffs = nx.clustering(g)
    counter = {}
    for t1 in np.arange(0, 1.1, 0.1):
        counter[round(t1,1)] = 0

    for coeff in clustering_coeffs.values():
        c = round(coeff,1)
        counter[c] += 1

    plt.subplot(1, 1, i)
    plt.bar(np.arange(0, 1.1, 0.1), counter.values(), color ='green', width = 0.4)
    plt.title(f'Clustering Coefficient Distribution Histogram for \n{t}')
    plt.xlabel('Clustering Coefficient')
    plt.ylabel('Frequency')

show_dist(rwg,1,"(High Energy Physics - Phenomenology) collaboration network dataset")
plt.show()