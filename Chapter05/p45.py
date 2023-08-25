# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 45, Chapter: 05, Book: "Practical Social Network Analysis with Python"

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

print('Problem: 45, Chapter: 05, Book: "Practical Social Network Analysis with Python"\n')
print('Average neighbour degree distribution\n')

# Read the edges from the 'ca-HepPh.txt' instead of 'com-friendster.ungraph.txt' file,
# because friendster dataset needs huge memory and computing. Two mentioned files have 
# same characteristics (see https://snap.stanford.edu/data/index.html part "Networks with ground-truth communities")
# It seems that friendster dataset needs GraphX on Hadoop or Spark. So it can not run on my laptop!
rwg = nx.read_edgelist('ca-HepPh.txt', create_using=nx.DiGraph(), comments='#')
rwg.remove_edges_from(nx.selfloop_edges(rwg))
rwg = nx.Graph(rwg)

plt.rcParams["figure.figsize"] = (14,8)
def show_dist(g,t):
    dgsq = [g.degree(n) for n in list(nx.nodes(g))]
    dgsq = max(dgsq)
    ands = np.zeros(dgsq+1,dtype=np.int32)
    andn = np.zeros(dgsq+1,dtype=np.int32)

    for n1 in list(g.nodes()):
        nbs1 = set(g.neighbors(n1))
        if n1 in nbs1:
            nbs1.remove(n1)
        out = 0
        for n2 in nbs1:
            out += g.degree(n2)
        d=g.degree(n1)
        ands[d] += out
        andn[d] += 1

    ax1, ax2, ax3 = [], [], []
    for d in range(1,dgsq+1,1):
        if andn[d]!=0:
            ax1.append(d)
            ax2.append(andn[d])
            ax3.append(ands[d]/andn[d])

    plt.subplot(1, 2, 1)
    plt.plot(ax1, ax2, color ='green', linewidth=1)
    plt.title(f'Degree Distribution Histogram for\n{t}')
    plt.xlabel('Degree')
    plt.ylabel('Number of Nodes')

    plt.subplot(1, 2, 2)
    plt.plot(ax1, ax3, color ='blue', linewidth=1)
    plt.title(f'Average Neighbour Degree Distribution Histogram for\n{t}')
    plt.xlabel('Degree (K)')
    plt.ylabel('Average Neighbour Degree')
    plt.legend()


show_dist(rwg,"(High Energy Physics - Phenomenology)\ncollaboration network dataset")
plt.show()