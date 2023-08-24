# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 33, Chapter: 04, Book: "Practical Social Network Analysis with Python"

import networkx as nx
import matplotlib.pyplot as plt

print('Problem: 33, Chapter: 04, Book: "Practical Social Network Analysis with Python"\n')
print('Degree distribution\n')

# read the edges from the 'CA-AstroPh.txt' file
rwg = nx.read_edgelist('CA-GrQc.txt', create_using=nx.Graph(), comments='#')

rwg_nodes = len(rwg.nodes())

swg = nx.watts_strogatz_graph(rwg_nodes, 5, 0.5, seed=10)

plt.rcParams["figure.figsize"] = (10,5)
def show_dist(g,i,t):
    dgsq = [g.degree(n) for n in nx.nodes(g)]
    plt.subplot(1, 2, i)
    plt.hist(dgsq, bins=max(dgsq), color ='red')
    plt.title(f'Degree Distribution Histogram for \n{t}')
    plt.xlabel('Degree')
    plt.ylabel('Frequency')

show_dist(rwg,1,"Real World Graph")
show_dist(swg,2,"Small World Graph")
plt.show()