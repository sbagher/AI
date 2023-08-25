# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 44, Chapter: 05, Book: "Practical Social Network Analysis with Python"

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

print('Problem: 44, Chapter: 05, Book: "Practical Social Network Analysis with Python"\n')
print('Average friends-of-friends distribution\n')

# Read the edges from the 'ca-HepPh.txt' instead of 'com-friendster.ungraph.txt' file,
# because friendster dataset needs huge memory and computing. Two mentioned files have 
# same characteristics (see https://snap.stanford.edu/data/index.html part "Networks with ground-truth communities")
# It seems that friendster dataset needs GraphX on Hadoop or Spark. So it can not run on my laptop!
rwg = nx.read_edgelist('ca-HepPh.txt', create_using=nx.DiGraph(), comments='#')
rwg.remove_edges_from(nx.selfloop_edges(rwg))
rwg = nx.Graph(rwg)

plt.rcParams["figure.figsize"] = (14,8)
def show_dist(g,t):
    dgsq = [g.degree(n) for n in nx.nodes(g)]
    dgsq = max(dgsq)
    fofs1 = np.zeros(dgsq+1,dtype=np.int32)
    fofs2 = np.zeros(dgsq+1,dtype=np.int32)
    fofn = np.zeros(dgsq+1,dtype=np.int32)

    for n1 in g.nodes:
        nbs1 = set(g.neighbors(n1))
        if n1 in nbs1:
            nbs1.remove(n1)
        nbs3 = set()
        out = 0
        for n2 in nbs1:
            nbs2 = set(g.neighbors(n2))
            nbs2.remove(n1)
            out += len(nbs2)
            nbs3 |= nbs2
        d=g.degree(n1)
        fofs1[d] += len(nbs3)
        fofs2[d] += out
        fofn[d] += 1

    ax1, ax2, ax3, ax4, ax5 = [], [], [], [], []
    for d in range(1,dgsq+1,1):
        if fofn[d]!=0:
            ax1.append(d)
            ax2.append(fofn[d])
            ax3.append(fofs1[d]/fofn[d])
            ax4.append(fofs2[d]/fofn[d])
            ax5.append(d*d)

    plt.subplot(1, 2, 1)
    plt.plot(ax1, ax2, color ='green', linewidth=1)
    plt.title(f'Number of friends-of-friends (NFoF) \n{t}')
    plt.xlabel('Degree')
    plt.ylabel('NFoF')

    plt.subplot(1, 2, 2)
    plt.plot(ax1, ax3, label = "Unique FoFs")
    plt.plot(ax1, ax4, label = "Non-Unique FoFs")
    #plt.plot(ax1, ax5, color ='blue', linewidth=1, label = "K2")
    plt.title(f'Average Friends-of-Friends (AFoF)\nDistribution Histogram for\n{t}')
    plt.xlabel('Degree (K)')
    plt.ylabel('AFoF')
    plt.legend()


show_dist(rwg,"(High Energy Physics - Phenomenology)\ncollaboration network dataset")
plt.show()