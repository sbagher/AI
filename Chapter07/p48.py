# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 48, Chapter: 07, Book: "Practical Social Network Analysis with Python"

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

print('Problem: 48, Chapter: 07, Book: "Practical Social Network Analysis with Python"\n')
print('Calculate the fraction of positive and negative edges in the graph. Let the fraction\n\
of positive edges be p. Assuming that each edge of a triad will independently be.\n\
assigned a positive sign with probability p and a negative sign with probability\n\
1 − p, calculate the probability of each type of triad.\n')

# read the edges from the 'soc-sign-epinions.txt' file
g = nx.read_edgelist('soc-sign-epinions.txt', create_using=nx.MultiGraph(), comments='#', nodetype=int, data=(("sign", int),))
g.remove_edges_from(nx.selfloop_edges(g))

p, n = 0, 0
for u, v, keys, sign in g.edges(data="sign", keys=True):
    if sign == 1:
        p += 1
    else:
        n += 1

t = p + n
p, n = p/t, n/t
print (f"fraction of positive edges:{p}")
print (f"fraction of negative edges:{n}")

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

t = t0 + t1 + t2 + t3

t4, t5, t6, t7 = 0, 0, 0, 0
for i in range (t):
    s1, s2, s3 = np.random.uniform(0,1,3) < p
    # t7: +++
    # t6: ++-
    # t5: +--
    # t4: ---
    if s1:
        if s2:
            if s3:
                t7 += 1
            else:
                t6 += 1
        else:
            if s3:
                t6 += 1
            else:
                t5 += 1
    else:
        if s2:
            if s3:
                t6 += 1
            else:
                t5 += 1
        else:
            if s3:
                t5 += 1
            else:
                t4 += 1

tt = t4 + t5 + t6 + t7

print ("Ti\t\t|Ti|\t\tp(Ti)\t\t|T0i|\t\tp0(Ti)")
print (f"T3+++\t\t{t3}\t\t{np.round(t3/t,3)}\t\t{t7}\t\t{np.round(t7/tt,3)}")
print (f"T2++-\t\t{t2}\t\t{np.round(t2/t,3)}\t\t{t6}\t\t{np.round(t6/tt,3)}")
print (f"T1+--\t\t{t1}\t\t{np.round(t1/t,3)}\t\t{t5}\t\t{np.round(t5/tt,3)}")
print (f"T0---\t\t{t0}\t\t{np.round(t0/t,3)}\t\t{t4}\t\t{np.round(t4/tt,3)}")