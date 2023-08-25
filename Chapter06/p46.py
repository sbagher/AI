# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 46, Chapter: 06, Book: "Practical Social Network Analysis with Python"

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random

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
    t = 1023
    for i in range(1,11,1):
        t = t<<1
        if (v & t)==(u & t):
            return i

def create_graph (a):
    g = nx.DiGraph()
    p = np.zeros(11, dtype=np.float32)
    for i in range(1,11,1):
        p[i] = 2 ** (-a*i)

    l = np.arange(1000)
    for n in range(0,1000,1):
        g.add_node(n)

    np.random.shuffle(l)

    i = -1
    ps = 0.0
    for n1 in list(nx.nodes(g)):
        k = 0
        while k != 5:
            i += 1
            if i == 1000:
                i = 0
            n2 = int(l[i])
            if n1 != n2:
                if not (g.has_edge(n1, n2) or g.has_edge(n2, n1)):
                    ps += p[int(h(n1,n2))]
                    if ps >= 1:
                        g.add_edge(n1,n2)
                        k += 1
                        ps = 0
    return g

def run_search(a):
    g = create_graph (a)
    nodes = list(g.nodes)
    node_pairs = []
    i = 0
    while i!= 1000:
        u, v = random.sample(nodes, 2)
        t = (u, v)
        if not (v == u or t in node_pairs):
            node_pairs.append(t)
            i += 1

    SuccessHopsSum = 0
    SuccessHopsNum = 0
    for s, t in node_pairs:
        hops = 0
        while True:
            hops += 1
            sn = set(g.neighbors(s))
            um = -1
            m = 11
            for u in sn:
                if h(s,u)<m:
                    m = h(s,u)
                    um = u
            if um == t:
                SuccessHopsSum += hops
                SuccessHopsNum += 1
                break
            else:
                if h(s, t) > h(um, t):
                    s = um
                else:
                    break
    return SuccessHopsSum, SuccessHopsNum

ax1, ax2, ax3 = [], [], []
for aa in np.arange (0.1, 2.1, 0.1):
    a = round(aa,1)
    print (a)
    s, n = run_search(a)
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
plt.title(f'Average Path Length Histogram')
plt.xlabel('α')
plt.ylabel('search success probability')
plt.show()