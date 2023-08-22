# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 27, Chapter: 03, Book: "Practical Social Network Analysis with Python"

import networkx as nx
import matplotlib.pyplot as plt

print('Problem: 26, Chapter: 03, Book: "Practical Social Network Analysis with Python"\n')
print('Shortest path length distributions\n')

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
    clustering_coeffs = nx.clustering(g)
    counter = {}

    for coeff in round(clustering_coeffs.values(),1):
        if coeff in counter.keys():
            counter[coeff]  += 1
        else:
            counter[coeff] = 1

    plt.hist(list(clustering_coeffs.values()), bins=max(list(counter.values())))
    plt.title('Clustering coefficient distribution')
    plt.xlabel('Clustering coefficient')
    plt.ylabel('Frequency')
    plt.show()
    plt.subplot(1, 3, i)
    plt.hist(path_lengths, bins=max(path_lengths))
    plt.title(f'Shortest Path Length Distribution Histogram for \n{t}')
    plt.xlabel('Path Length')
    plt.ylabel('Frequency')
show_dist(rwg,1,"real world graph")
show_dist(rg,2,"Erdös–Rényi random graph")
show_dist(cg,3,"Conﬁguration model random graph")
plt.show()