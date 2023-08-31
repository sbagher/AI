# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 46, Chapter: 06, Book: "Practical Social Network Analysis with Python"

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
import time

print('Problem: 46, Chapter: 06, Book: "Practical Social Network Analysis with Python"\n')
print('Create random networks for α = 0.1, 0.2, ... , 10. For each of these networks,\n\
sample 1000 unique random (s, t) pairs (s != t). Then do a decentralized search\n\
starting from s as follows. Assuming that the current node is s, pick its neighbour\n\
u with smallest h(u, t) (break ties arbitrarily). If u = t, the search succeeds. If\n\
h(s, t) > h(u, t), set s to u and repeat. If h(s, t) ≤ h(u, t), the search fails.\n\n\
For each α, pick 1000 pairs of nodes and compute the average path length for the\n\
searches that succeeded. Then draw a plot of the average path length as a function\n\
of α. Also, plot the search success probability as a function of α.\n')

def h (v,u):
    if u == v:
        return 0
    t = 1023
    for i in range(1,11,1):
        t = t<<1
        if (v & t)==(u & t):
            return i

def create_graph (a):
    g = nx.DiGraph()

    p = np.zeros(11, dtype=np.float64)
    for l in range(1,11,1):
        p[l] = 2 ** (-a*l)

    ordered_levels = np.flip(np.argsort(p))

    nodes = list(range(0,1024,1))
    while len (nodes) != 1000:
        node = random.randint(0,1024)
        if node in nodes:
            nodes.remove(node)

    for node in nodes:
        g.add_node(node)

    shape = (11, 1024, 512)
    related_nodes_in_level = np.empty(shape, dtype=np.int16)
    shape = (11, 1024)
    last_item = np.zeros(shape, dtype=np.int16)
    nodes_in_level = np.zeros(11, dtype=np.int64)
    for n1 in nodes:
        for n2 in nodes:
            if n1 != n2:
                t = h(n1,n2)
                related_nodes_in_level[t][n1][last_item[t][n1]] = n2
                last_item[t][n1] += 1
                nodes_in_level[t] += 1

    sum_of_probabilities = 0
    for l in range(1,11,1):
        sum_of_probabilities += p[l] * nodes_in_level[l]

    b = 0
    sum_of_egdes = 0
    max_edges = 5000
    level_capacity = np.zeros(11, dtype=np.int16)
    while abs(max_edges-sum_of_egdes) > 5:
        sum_of_egdes = 0
        for l in range(1,11,1):
            level_capacity[l] = round(p[l] * (max_edges+b) / sum_of_probabilities * nodes_in_level[l], 0)
            sum_of_egdes += int(level_capacity[l])
        b = max_edges-sum_of_egdes

    for l in ordered_levels[:11]:
        if sum_of_egdes < 5000:
            level_capacity[l] += 1
            sum_of_egdes += 1
        if sum_of_egdes > 5000 and level_capacity[l] != 0:
            level_capacity[l] -= 1
            sum_of_egdes -= 1
        if sum_of_egdes == 5000:
            break

    in_capacity_used = np.zeros(1024, dtype=np.int8)
    out_capacity_used = np.zeros(1024, dtype=np.int16)
    created_edges = 0
    for l in ordered_levels[:1]:
        out_permitted_nodes = []
        for n1 in nodes:
            related_as_in_nodes = related_nodes_in_level[l][n1][:last_item[l][n1]+1]
            in_c = 0
            for n2 in related_as_in_nodes:
                if in_capacity_used[n2] < 5:
                    in_c += 1
            out_c = out_capacity_used[n1]
            while out_c < 5 and in_c > 0:
                out_c += 1
                in_c -= 1
                out_permitted_nodes.append(n1)
        random.shuffle()

        while level_capacity[l] != 0 and out_permitted_nodes:
            n1 = out_permitted_nodes.pop()
            related_as_in_nodes = related_nodes_in_level[l][n1][:last_item[l][n1]+1]
            for n2 in related_as_in_nodes:
                if in_capacity_used[n2] < 5:
                    g.add_edge(n1,n2)
                    level_capacity[l] -= 1
                    in_capacity_used[n2] += 1
                    out_capacity_used[n1] += 1
                    created_edges += 1

        if level_capacity[l] != 0:
            sum_of_probabilities = 0
            for lt in ordered_levels[l+1:11]:
                sum_of_probabilities += p[lt] * nodes_in_level[lt]

            b = 0
            sum_of_egdes = 0
            max_edges = 5000 - created_edges
            level_capacity = np.zeros(11, dtype=np.int16)
            while abs(max_edges-sum_of_egdes) > 5:
                sum_of_egdes = 0
                for lt in ordered_levels[l+1:11]:
                    level_capacity[lt] = round(p[lt] * (max_edges+b) / sum_of_probabilities * nodes_in_level[lt], 0)
                    sum_of_egdes += int(level_capacity[lt])
                b = max_edges-sum_of_egdes

            for lt in ordered_levels[l+1:11]:
                if sum_of_egdes < 5000:
                    level_capacity[lt] += 1
                    sum_of_egdes += 1
                if sum_of_egdes > 5000 and level_capacity[lt] != 0:
                    level_capacity[lt] -= 1
                    sum_of_egdes -= 1
                if sum_of_egdes == 5000:
                    break

    return g

def create_node_pairs(g):
    nodes = list(g.nodes())
    node_pairs = []
    i = 0
    while i!= 1000:
        u, v = random.sample(nodes, 2)
        t = (u, v)
        if not (v == u or t in node_pairs):
            node_pairs.append(t)
            i += 1

    return node_pairs

def run_search(g, node_pairs):
    SuccessHopsSum = 0
    SuccessSum = 0
    for s, t in node_pairs:
        hops = 0
        while True:
            hops += 1
            sn = set(g.neighbors(s))
            um = -1
            m = 11
            for u in sn:
                if h(u,t) < m:
                    m = h(u,t)
                    um = u
            if um == t:
                SuccessHopsSum += hops
                SuccessSum += 1
                break
            else:
                if h(s, t) > h(um, t):
                    s = um
                else:
                    break
    return SuccessHopsSum, SuccessSum

ax1, ax2, ax3 = [], [], []
for aa in np.arange (0.1, 10.1, 0.1):
    a = round(aa,1)
    start = time.time()
    g = create_graph (a)
    for n in g.nodes():
        if g.out_degree(n)!=5:
            print ("Jing",g.out_degree(n))
    node_pairs = create_node_pairs(g)
    s, n = run_search(g, node_pairs)
    end = time.time()
    print(a, end - start)    
    ax1.append(a)
    if n==0:
        ax2.append(0.0)
        ax3.append(0.0)
    else:
        ax2.append(s/n)
        ax3.append(n/1000)

plt.rcParams["figure.figsize"] = (14,8)
plt.subplot(1, 2, 1)
plt.plot(ax1, ax2, color ='green', linewidth=1)
plt.title(f'Average Path Length Histogram')
plt.xlabel('α')
plt.ylabel('Average Path Length')

plt.subplot(1, 2, 2)
plt.plot(ax1, ax3, color ='blue', linewidth=1)
plt.title(f'Search Success Probability Histogram')
plt.xlabel('α')
plt.ylabel('search success probability')
plt.show()