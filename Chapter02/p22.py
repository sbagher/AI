# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 22, Chapter: 02, Book: "Practical Social Network Analysis with Python"

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# read the edges from the 'soc-Epinions1.txt' file
G = nx.read_edgelist('soc-Epinions1.txt', create_using=nx.DiGraph(), comments='#')

print('Problem: 22, Chapter: 02, Book: "Practical Social Network Analysis with Python"\n')
print('Compute the in-degree and out-degree distributions and plot the power law for each of these distributions.')

def run_in_out(func,color,lable):
    in_out = dict(func())
    max_degree = max(in_out.values())
    freq=np.zeros(max_degree + 1)
    for degree in in_out.values():
        freq[degree] += 1
    degree_prob=freq/sum(freq)
    # Plot the in-degree distribution
    plt.figure(figsize=(10, 5))
    plt.plot(range(len(degree_prob)), degree_prob, color)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel(f'{lable}-degree')
    plt.ylabel('Probability')
    plt.title(f'{lable}-degree Distribution')
    plt.grid(True)
    plt.show()

run_in_out(G.in_degree,'bo','In')
run_in_out(G.out_degree,'ro','Out')