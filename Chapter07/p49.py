# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 49, Chapter: 07, Book: "Practical Social Network Analysis with Python"


import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

print('Problem: 49, Chapter: 07, Book: "Practical Social Network Analysis with Python"\n')
print('Now, analyse a simple generative model of signed networks by running simulations\n\
of the dynamic process on small networks in the following manner. Create a\n\
complete network on 10 nodes. For each edge, choose a sign with uniform probability.\n\
Run this dynamic process for a million iterations. Repeat this process 100 times.\n\
What fraction of these networks are balanced?')

g = nx.complete_graph(10, nx.Graph())
g.remove_edges_from(nx.selfloop_edges(g))
edges = g.edges()
ec = len(edges)

unbalanced = 0
for _ in range(100):
    sp = []
    for p in np.random.uniform(0,1,1000000):
        sp = np.random.uniform(0,1,ec) < p

    i = 0
    for a, b in edges:
        if sp[i]:
            g[a][b]["sign"] = 1
        else:
            g[a][b]["sign"] = -1
        i += 1

    is_unbalanced = False
    for node in g.nodes:
        s = sorted(g.neighbors(node))
        i = 0
        for n in s:
            if n <= node:
                i += 1
        s = s[i:]
        while len(s) >= 2:
            n1 = s[0]
            for i in range(1,len(s)):
                n2 = s[i]
                s1 = g[node][n1]["sign"]
                s2 = g[node][n2]["sign"]
                s3 = g[n1][n2]["sign"]
                if (s1 * s2 * s3) < 0:
                    is_unbalanced = True
                    unbalanced += 1
                    break
            if is_unbalanced: break
            s = s[i:]            
        if is_unbalanced: break
print ("Number of balanced networks:", (100-unbalanced))
print ("Fraction of balanced networks:", np.round((100-unbalanced)/100,3))