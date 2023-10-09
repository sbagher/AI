# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 47, Chapter: 07, Book: "Practical Social Network Analysis with Python"


import networkx as nx
import matplotlib.pyplot as plt

print('Problem: 47, Chapter: 07, Book: "Practical Social Network Analysis with Python"\n')
print('Calculate the count and fraction of triads of each type in this network.\n')

# read the edges from the 'soc-sign-epinions.txt' file
g = nx.read_edgelist('soc-sign-epinions.txt', create_using=nx.MultiGraph(), comments='#', nodetype=int, data=(("sign", int),))
g.remove_edges_from(nx.selfloop_edges(g))

t0, t1, t2, t3 = 0, 0, 0, 0
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
            for k1 in g.get_edge_data(node, n1, default=[]):
                s1 = g.edges[node, n1, k1]["sign"]
                for k2 in g.get_edge_data(node, n2, default=[]):
                    s2 = g.edges[node, n2, k2]["sign"]
                    for k3 in g.get_edge_data(n1, n2, default=[]):
                        s3 = g.edges[n1, n2, k3]["sign"]
                        # t3: +++
                        # t2: ++-
                        # t1: +--
                        # t0: ---
                        if s1 == 1:
                            if s2 == 1:
                                if s3 == 1:
                                    t3 += 1
                                else:
                                    t2 += 1
                            else:
                                if s3 == 1:
                                    t2 += 1
                                else:
                                    t1 += 1
                        else:
                            if s2 == 1:
                                if s3 == 1:
                                    t2 += 1
                                else:
                                    t1 += 1
                            else:
                                if s3 == 1:
                                    t1 += 1
                                else:
                                    t0 += 1
        s = s[i:]            
