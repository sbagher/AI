# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 41, Chapter: 05, Book: "Practical Social Network Analysis with Python"

import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter

print('Problem: 41, Chapter: 05, Book: "Practical Social Network Analysis with Python"\n')
print('WCC size distributions\n')

# Read the edges from the 'ca-HepPh.txt' instead of 'com-friendster.ungraph.txt' file,
# because friendster dataset needs huge memory and computing. Two mentioned files have 
# same characteristics (see https://snap.stanford.edu/data/index.html part "Networks with ground-truth communities")
# It seems that friendster dataset needs GraphX on Hadoop or Spark. So it can not run on my laptop!
rwg = nx.read_edgelist('ca-HepPh.txt', create_using=nx.DiGraph(), comments='#')

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

show_dist(rwg,1,"(High Energy Physics - Phenomenology) collaboration network dataset")
plt.show()