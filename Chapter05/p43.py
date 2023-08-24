# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 43, Chapter: 05, Book: "Practical Social Network Analysis with Python"

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

print('Problem: 43, Chapter: 05, Book: "Practical Social Network Analysis with Python"\n')
print('k-core node size distribution\n')

# Read the edges from the 'ca-HepPh.txt' instead of 'com-friendster.ungraph.txt' file,
# because friendster dataset needs huge memory and computing. Two mentioned files have 
# same characteristics (see https://snap.stanford.edu/data/index.html part "Networks with ground-truth communities")
# It seems that friendster dataset needs GraphX on Hadoop or Spark. So it can not run on my laptop!
rwg = nx.read_edgelist('ca-HepPh.txt', create_using=nx.DiGraph(), comments='#')
rwg.remove_edges_from(nx.selfloop_edges(rwg))

plt.rcParams["figure.figsize"] = (10,5)
def show_dist(g,i,t):
    dgc = dict(nx.core_number(g))
    dgc = set(dgc.values())
    dgc = sorted(dgc, reverse=True)
    dgsqm = max(dgc)
    rwg_nodes = len(g.nodes())
    l=np.zeros(rwg_nodes+1,dtype=np.int32)

    for j in dgc:
        gt = nx.k_core(g, k=j)
        ll=len(gt.nodes())
        if ll!=0:
            l[ll] += 1

    ax1, ax2 = [], []
    for j in range (0,rwg_nodes,1):
        if l[j] != 0:
            ax1.append(j)
            ax2.append(l[j])

    plt.subplot(1, 1, i)
    plt.plot(ax1, ax2, color ='yellow', linewidth=3)
    plt.title(f'K-Core Node Size Distribution Histogram for \n{t}')
    plt.xlabel('Number of Nodes in K-Core')
    plt.ylabel('Frequency')

show_dist(rwg,1,"(High Energy Physics - Phenomenology) collaboration network dataset")
plt.show()