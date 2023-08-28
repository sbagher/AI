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

    sp = 0.0
    p = np.zeros(11, dtype=np.float64)
    for i in range(1,11,1):
        p[i] = 2 ** (-a*i)
        sp += p[i]

    b = 0
    sc = 0
    c = np.zeros(11, dtype=np.int16)
    while abs(5000-sc)>5:
        sc = 0
        f = (5000+b)/sp
        for i in range(1,11,1):
            c[i] = round(p[i] * f, 0)
            sc += int(c[i])
        b = 5000-sc

    for i in range(1,11,1):
        if sc < 5000:
            c[i] += 1
            sc += 1
        if sc > 5000:
            c[i] -= 1
            sc -= 1
        if sc == 5000:
            break

    nodes = list(range(0,1024,1))
    while len (nodes) != 1000:
        node = random.randint(0,1024)
        if node in nodes:
            nodes.remove(node)

    for node in nodes:
        g.add_node(node)

    shape = (1024,11)
    exist = np.zeros(shape, dtype=np.int16)
    for n1 in nodes:
        for n2 in nodes:
            exist [n1][h(n1,n2)] += 1

    shape = (1024,12)
    choosed = np.zeros(shape, dtype=np.int16)
    for l in range(1,11,1):
        rl = []
        for n1 in nodes:
            ex = exist[n1][l]
            ch = choosed[n1][11]
            while ex > 0 and ch < 5:
                ex -= 1
                ch += 1
                rl.append(n1)
        random.shuffle(rl)

        lrl = len(rl)
        if lrl < c[l]:
            c[l] = lrl
            sp = 0.0
            for i in range(l+1,11,1):
                sp += p[i]
            sc = 0
            for i in range(1,l+1,1):
                sc += c[i]
            nn = 5000 - sc
            b = 0
            sc = 0
            while abs(nn-sc)>5:
                sc = 0
                f = (nn+b)/sp
                for i in range(l+1,11,1):
                    c[i] = round(p[i] * f, 0)
                    sc += int(c[i])
                b = nn-sc

            for i in range(l+1,11,1):
                if sc < nn:
                    c[i] += 1
                    sc += 1
                if sc > nn:
                    c[i] -= 1
                    sc -= 1
                if sc == nn:
                    break
            
        cl = random.sample(rl, c[l])
        for n1 in cl:
            choosed[n1][l] += 1
            exist[n1][l] -= 1
            choosed[n1][11] += 1

    for n1 in nodes:
        r = np.empty(11, dtype=object)
        rl = []
        for l in range(0,11,1):
            r[l] = []
            ch = int(choosed[n1][l])
            while ch != 0:
                rl.append(l)
                ch -= 1
        for n2 in nodes:
            r[int(h(n1,n2))].append(n2)
        for l in rl:
            n2 = random.sample(r[l], 1)
            g.add_edge(n1,n2[0])
            r[l].remove(n2[0])

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