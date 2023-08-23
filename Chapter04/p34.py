# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 34, Chapter: 04, Book: "Practical Social Network Analysis with Python"

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

print('Problem: 34, Chapter: 04, Book: "Practical Social Network Analysis with Python"\n')
print('Short path length distribution\n')

# read the edges from the 'CA-AstroPh.txt' file
rwg = nx.read_edgelist('CA-GrQc.txt', create_using=nx.DiGraph(), comments='#')

rwg_nodes = len(rwg.nodes())

swg = nx.watts_strogatz_graph(rwg_nodes, 5, 0.5, seed=10)

plt.rcParams["figure.figsize"] = (15,5)
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

    plt.subplot(1, 2, i)
    plt.bar(range (0,maxl), l[0:maxl], color ='maroon', width = 0.4)
    plt.title(f'Shortest Path Length Distribution Histogram for \n{t}')
    plt.xlabel('Path Length')
    plt.ylabel('Frequency')

show_dist(rwg,1,"Real World Graph")
show_dist(swg,2,"Small World Graph")
plt.show()