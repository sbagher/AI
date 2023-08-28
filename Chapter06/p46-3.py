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
    for i in range(1,11,1):
        p[i] = 2 ** (-a*i)

    for n in range(0,1000,1):
        g.add_node(n)

    shape = (1000,11,11)
    hl = np.zeros(shape, dtype=np.int16)
    wpz = np.empty(1000, dtype=np.float64)
    shape = (1000,1)
    hs = np.empty(shape, dtype=np.float64)
    for n1 in range(0,1000,1):
        for i in range(0,10,1):
            for n2 in range(i*100,(i+1)*100,1):
                hl[n1][i][h(n1,n2)] += 1
        hls = 0
        wp = 0.0
        for l in range (1,11,1):
            for i in range(0,10,1):
                hls += hl[n1][i][l]
            hl[n1][10][l] = hls
            wp += hls*p[l]
        wpz[n1] = wp

    m = max (wpz)
    if m < 1:
        f = 1 / m
        for i in range(1,11,1):
            p[i] *= f

    for n1 in range(0,1000,1):
        wp = 0.0
        for l in range (1,11,1):
            wp += hl[n1][l]*p[l]
        wpz[n1] = wp

    n2 = -1
    ps = 0.0
    hlt = np.copy(hl)
    for n1 in range(0,1000,1):
        k = 0
        while k != 5:
            for i in range(0,10,1):
                if k == 5:
                    break
                cs = hst[n1][i]
                if (ps+cs) < 1:
                    ps += cs
                    continue 
                for n2 in range(i*100,(i+1)*100,1):
                    cc = ht[n1][n2]
                    if cc:
                        ps += cc
                        if ps >= 1:
                            g.add_edge(n1,n2)
                            ht[n1][n2] = 0
                            hst[n1][i:] -= cc
                            k += 1
                            if k == 5:
                                break
                            ps = 0
    return g

def run_search(a, node_pairs):
    g = create_graph (a)

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
                if h(u,t) < m:
                    m = h(u,t)
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

nodes = list(range(0,1000,1))
node_pairs = []
i = 0
while i!= 1000:
    u, v = random.sample(nodes, 2)
    t = (u, v)
    if not (v == u or t in node_pairs):
        node_pairs.append(t)
        i += 1

ax1, ax2, ax3 = [], [], []
for aa in np.arange (0.1, 10.1, 0.1):
    a = round(aa,1)
    start = time.time()
    s, n = run_search(a, node_pairs)
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