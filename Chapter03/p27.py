# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 27, Chapter: 03, Book: "Practical Social Network Analysis with Python"

import networkx as nx
import matplotlib.pyplot as plt

print('Problem: 27, Chapter: 03, Book: "Practical Social Network Analysis with Python"\n')
print('Degree distributions\n')

# read the edges from the 'CA-AstroPh.txt' file
rwg = nx.read_edgelist('CA-AstroPh.txt', create_using=nx.DiGraph(), comments='#')
rwg_nodes = len(rwg.nodes())
rwg_edges = len(rwg.edges())
ind = [rwg.in_degree(n) for n in nx.nodes(rwg)]
outd = [rwg.out_degree(n) for n in nx.nodes(rwg)]

rg = nx.gnm_random_graph(rwg_nodes,rwg_edges,seed=10,directed=True)

cg = nx.directed_configuration_model (ind,outd,seed=10)

plt.rcParams["figure.figsize"] = (15,5)
def show_dist(g,i,t):
    dgsq = [g.degree(n) for n in nx.nodes(g)]
    plt.subplot(1, 3, i)
    plt.hist(dgsq, bins=max(dgsq), color ='red')
    plt.title(f'Degree Distribution Histogram for \n{t}')
    plt.xlabel('Degree')
    plt.ylabel('Frequency')
show_dist(rwg,1,"Real World Graph")
show_dist(rg,2,"Erdös–Rényi Random Graph")
show_dist(cg,3,"Conﬁguration Model Random Graph")
plt.show()