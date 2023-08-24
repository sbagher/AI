# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 42, Chapter: 05, Book: "Practical Social Network Analysis with Python"

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

print('Problem: 40, Chapter: 05, Book: "Practical Social Network Analysis with Python"\n')
print('Shortest path length distribution\n')

# Read the edges from the 'ca-HepPh.txt' instead of 'com-friendster.ungraph.txt' file,
# because friendster dataset needs huge memory and computing. Two mentioned files have 
# same characteristics (see https://snap.stanford.edu/data/index.html part "Networks with ground-truth communities")
# It seems that friendster dataset needs GraphX on Hadoop or Spark. So it can not run on my laptop!
rwg = nx.read_edgelist('ca-HepPh.txt', create_using=nx.DiGraph(), comments='#')

plt.rcParams["figure.figsize"] = (10,5)
def show_dist(g,i,t):
    l=np.zeros(100,dtype=np.ulonglong)
    for n in g.nodes:
        lengths = nx.shortest_path_length(g, n)
        for j in list(lengths.values()):
            l[j] += 1

    maxl=0
    for j in range (99,0,-1):
        if l[j] != 0:
            maxl=j
            break

    plt.subplot(1, 1, i)
    plt.bar(range (0,maxl), l[0:maxl], color ='maroon', width = 0.4)
    plt.title(f'Shortest Path Length Distribution Histogram for \n{t}')
    plt.xlabel('Path Length')
    plt.ylabel('Frequency')

show_dist(rwg,1,"(High Energy Physics - Phenomenology) collaboration network dataset")
plt.show()