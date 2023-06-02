import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G = nx.read_edgelist('soc-Epinions1.txt', create_using=nx.DiGraph())

def run_in_out(in_out,color,lable):
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

run_in_out(dict(G.in_degree()),'bo','In')
run_in_out(dict(G.out_degree()),'ro','Out')