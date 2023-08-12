# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 59, Chapter: 11, Book: "Practical Social Network Analysis with Python"

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

print('Problem: 59, Chapter: 11, Book: "Practical Social Network Analysis with Python"\n')
print('Repeat the experiments by initialising the infected set to be 10 random nodes \
and the top 10 highest degree nodes, respectively. Calculate the total percentage of \
nodes that became infected in each simulation.')

# read the edges from the 'com-dblp.ungraph.txt' file
G = nx.read_edgelist('com-dblp.ungraph.txt', create_using=nx.DiGraph(), comments='#')

print('Number of nodes:', len(G.nodes()))
print('Number of edges:', len(G.edges()))

def SIRModel(G,I):
    b = 20
    g = 2
    c1 = 0
    c2 = 0
    S = G.nodes() - I
    R = set()
    while I:
        SP = set()
        IP = set()
        JP = set()
        RP = set()
        for u in G.nodes():
            if u in S:
                for v in G.neighbors(u):
                    if v in I:
                        c1 += 1
                        if c1 % b == 0:
                            SP |= set(u)
                            IP |= set(u)
            else:
                if u in I:
                    for v in G.neighbors(u):
                        if v in S:
                            c1 += 1
                            if c1 % b == 0:
                                SP |= {v}
                                IP |= {v}
                    c2 += 1
                    if c2 % g == 0:
                        JP |= {u}
                        RP |= {u}
        S -= SP
        I = (I|IP)-JP
        R |= RP
    print(len(R))

g=set(G.neighbors('0'))
print (g)

SIRModel(G,{'0'})