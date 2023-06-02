import networkx as nx
import matplotlib.pyplot as plt
import random
from collections import Counter

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
f1= [0 for d in range(max(dgsq1)+1)]
for d in dgsq1:
    f1[d] += 1

plt.hist(f1, bins=max(f1)+1)
plt.title('In-Degree Histogram')
plt.xlabel('In-Degree')
plt.ylabel('Frequency')
plt.show()

# Q8: Out-degree distribution
print('\nQ8: Out-degree distribution')
dgsq2 = [G.out_degree(n) for n in nx.nodes(G)]
f2= [0 for d in range(max(dgsq2)+1)]
for d in dgsq2:
    f2[d] += 1

plt.figure() 
plt.hist(f2, bins=max(f2)+1)
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
