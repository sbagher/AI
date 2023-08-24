# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 36, Chapter: 04, Book: "Practical Social Network Analysis with Python"

import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter

print('Problem: 36, Chapter: 04, Book: "Practical Social Network Analysis with Python"\n')
print('WCC size distributions\n')

# read the edges from the 'CA-AstroPh.txt' file
rwg = nx.read_edgelist('CA-GrQc.txt', create_using=nx.Graph(), comments='#')

rwg_nodes = len(rwg.nodes())

swg = nx.watts_strogatz_graph(rwg_nodes, 5, 0.5, seed=10)
swg = nx.DiGraph(swg)

plt.rcParams["figure.figsize"] = (15,5)
def show_dist(g,i,t):
    wccs = list(nx.weakly_connected_components(g))

    wcc_sizes = [len(wcc) for wcc in wccs]
    wcc_size_counts = Counter(wcc_sizes)
    l = map(str, wcc_size_counts.keys())
    l = list(l)

    plt.subplot(1, 2, i)
    plt.bar(l, wcc_size_counts.values(), color ='blue', width = 0.4)
    plt.title(f'WCC Size Distribution Histogram for \n{t}')
    plt.xlabel('WCC Size')
    plt.ylabel('Frequency')

show_dist(rwg,1,"Real World Graph")
show_dist(swg,2,"Small World Graph")
plt.show()