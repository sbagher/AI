# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 39, Chapter: 05, Book: "Practical Social Network Analysis with Python"

import networkx as nx
import matplotlib.pyplot as plt

print('Problem: 39, Chapter: 05, Book: "Practical Social Network Analysis with Python"\n')
print('Degree distribution\n')

# Read the edges from the 'ca-HepPh.txt' instead of 'com-friendster.ungraph.txt' file,
# because friendster dataset needs huge memory and computing. Two mentioned files have 
# same characteristics (see https://snap.stanford.edu/data/index.html part "Networks with ground-truth communities")
# It seems that friendster dataset needs GraphX on Hadoop or Spark. So it can not run on my laptop!
rwg = nx.read_edgelist('ca-HepPh.txt', create_using=nx.DiGraph(), comments='#')

plt.rcParams["figure.figsize"] = (10,5)
def show_dist(g,i,t):
    dgsq = [g.degree(n) for n in nx.nodes(g)]
    plt.subplot(1, 1, i)
    plt.hist(dgsq, bins=max(dgsq), color ='red')
    plt.title(f'Degree Distribution Histogram for \n{t}')
    plt.xlabel('Degree')
    plt.ylabel('Frequency')

show_dist(rwg,1,"(High Energy Physics - Phenomenology) collaboration network dataset")
plt.show()