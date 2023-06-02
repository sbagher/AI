import networkx as nx
import matplotlib.pyplot as plt
import random
from collections import Counter
import numpy as np

# read the edges from the 'email-Eu-core.txt' file
G = nx.read_edgelist('email-Eu-core.txt', create_using=nx.DiGraph())

# Q1: Number of nodes
print('\nQ1: Number of nodes: ', len(G.nodes()))

# Q2: Number of edges
print('\nQ2: Number of edges:', len(G.edges()))

# Q3: In-degree, out-degree and degree of the first five nodes
print('\nQ3: In-degree, out-degree and degree of the first five nodes')
for n in list(G.nodes)[0:5]:
    print('\tnode:', n, '{in-degree:', G.in_degree(n), 'out-degree:', G.out_degree(n), 'degree:', G.degree(n),"}")

# Q4: Number of source nodes
src = []
for n in G.nodes():
    if G.in_degree(n) == 0:
        src.append(n)
print('\nQ4: Number of source nodes: ', len(src))

# Q5: Number of sink nodes
snk = []
for n in G.nodes():
    if G.out_degree(n) == 0:
        snk.append(n)
print('\nQ5: Number of sink nodes: ', len(snk))

# Q6: Number of isolated nodes
isl = []
for n in G.nodes():
    if G.degree(n) == 0:
        isl.append(n)
print('\nQ6: Number of isolated nodes: ', len(isl))

# Q7: In-degree distribution
print('\nQ7: In-degree distribution')
dgsq1 = [G.in_degree(n) for n in nx.nodes(G)]
plt.hist(dgsq1, bins=max(dgsq1))
plt.title('In-Degree Histogram')
plt.xlabel('In-Degree')
plt.ylabel('Frequency')
plt.show()

# Q8: Out-degree distribution
print('\nQ8: Out-degree distribution')
dgsq2 = [G.out_degree(n) for n in nx.nodes(G)]
plt.hist(dgsq2, bins=max(dgsq2))
plt.title('Out-Degree Histogram')
plt.xlabel('Out-Degree')
plt.ylabel('Frequency')
plt.show()

# Q9: Average degree, average in-degree and average out-degree
print('\nQ9: Average degree, average in-degree and average out-degree')
print("\tAverage degree: ", sum([G.degree(n) for n in nx.nodes(G)]) / len(G.nodes))
print("\tAverage in-degree: ", sum([G.in_degree(n) for n in nx.nodes(G)]) / len(G.nodes))
print("\tAverage out-degree: ", sum([G.out_degree(n) for n in nx.nodes(G)]) / len(G.nodes))


# Q10: Distance between five pairs of random nodes
nodes = list(G.nodes)
node_pairs = []
for i in range(5):
    pair = random.sample(nodes, 2)
    node_pairs.append(tuple(pair))
    
print("\nQ10: Distance between five pairs of random nodes\n", node_pairs)

for pair in node_pairs:
    source, target = pair
    try:
        distance = nx.shortest_path_length(G, source=source, target=target)
        print(f"Distance between nodes {source} and {target}: {distance}")
    except nx.NodeNotFound as e:
        print(f"Node not found: {e}")
    except nx.NetworkXNoPath as e:
        print(f"No path found: {e}")

# Q11: Shortest path length distribution
print('\nQ11: Shortest path length distribution')
path_lengths = []
for node in G.nodes:
    lengths = nx.shortest_path_length(G, node)
    path_lengths += list(lengths.values())

path_length_counts = Counter(path_lengths)
for length, count in sorted(path_length_counts.items()):
    print(f"{length}: {count}")

# Q12: Diameter
print('\nQ12: Diameter:',max(path_length_counts))

# Q13: Is the graph strongly connected? If so, compute the strongly connected component size distribution
print('\nQ13: Is the graph strongly connected? If so, compute the strongly connected component size distribution\n')

if nx.is_strongly_connected(G):
    print("The graph is strongly connected.")
else:
    sccs = list(nx.strongly_connected_components(G))

    scc_sizes = [len(scc) for scc in sccs]
    scc_size_counts = Counter(scc_sizes)

    print("The graph is not strongly connected. Strongly connected component size distribution:")
    for size, count in sorted(scc_size_counts.items()):
        print(f"\t{size}: {count}")

# Q14: Is the graph weakly connected? If so, compute the weakly connected component size distribution
print('\nQ14: Is the graph weakly connected? If so, compute the weakly connected component size distribution\n')

if nx.is_weakly_connected(G):
    print("The graph is weakly connected.")
else:
    wccs = list(nx.weakly_connected_components(G))

    wcc_sizes = [len(wcc) for wcc in wccs]
    wcc_size_counts = Counter(wcc_sizes)

    print("The graph is not weakly connected. Weakly connected component size distribution:")
    for size, count in sorted(wcc_size_counts.items()):
        print(f"\t{size}: {count}")

# Q15: Number of bridge edges
G_undirected = G.to_undirected(as_view=True)
bridges = list(nx.bridges(G_undirected))
print(f"\nQ15: Number of bridge edges: {len(bridges)}")

# Q16: Number of articulation nodes
articulation_nodes = list(nx.articulation_points(G_undirected))
print(f"\nQ16: Number of articulation nodes: {len(articulation_nodes)}")

# Q17: Number of nodes in In(v) for five random nodes
print('\nQ17: Number of nodes in In(v) for five random nodes')
random_nodes = random.sample(list(G.nodes()), 5)

for node in random_nodes:
    in_neighbors = G.predecessors(node)
    print(f"\tNumber of nodes in In({node}): {len(list(in_neighbors))}")

# Q18: Number of nodes in Out (v) for five random nodes
print('\nQ18: Number of nodes in Out (v) for five random nodes')
random_nodes = random.sample(list(G.nodes()), 5)

for node in random_nodes:
    out_neighbors = G.successors(node)
    print(f"\tNumber of nodes in Out({node}): {len(list(out_neighbors))}")

# Q19: Clustering coefficient for five random nodes
print('\nQ19: Clustering coefficient for five random nodes')
random_nodes = random.sample(list(G.nodes()), 5)

for node in random_nodes:
    print(f"\tClustering coefficient of node {node}: {nx.clustering(G, node)}")

# Q20: Clustering coefficient distribution
print('\nQ20: Clustering coefficient distribution')
clustering_coeffs = nx.clustering(G)
print(clustering_coeffs)
for node, coeff in clustering_coeffs.items():
        print(f"\t{node}: {coeff}")