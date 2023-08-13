# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 59, Chapter: 11, Book: "Practical Social Network Analysis with Python"

import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np

print('Problem: 59, Chapter: 11, Book: "Practical Social Network Analysis with Python"\n')
print('Repeat the experiments by initialising the infected set to be 10 random nodes \
and the top 10 highest degree nodes, respectively. Calculate the total percentage of \
nodes that became infected in each simulation.')

def SIRModel_Book(G,I):
    b = 20
    g = 2
    c1 = random.choice(range(b))
    c2 = random.choice(range(g))
    S = G.nodes() - I
    R = set()
    while I:
        SP = set()
        IP = set()
        JP = set()
        RP = set()
        for u in G.nodes():
            if u in S:
                for v in G.successors(u):
                    if v in I:
                        c1 += 1
                        if c1 % b == 0:
                            SP |= {u}
                            IP |= {u}
            else:
                if u in I:
                    c2 += 1
                    if c2 % g == 0:
                        JP |= {u}
                        RP |= {u}
        S -= SP
        I = (I|IP)-JP
        R |= RP
    print(len(R))

def SIRModel_Corrected(G,I):
    b = 5
    g = 50
    c1 = random.choice(range(b))
    c2 = random.choice(range(g))
    S = G.nodes() - I
    R = set()
    while I:
        SP = set()
        IP = set()
        JP = set()
        RP = set()
        for i in I:
            for n in set(G.neighbors(i)) | set(G.predecessors(i)) | set(G.successors(i)):
                if n in S:
                    c1 += 1
                    if c1 == b:
                        SP |= {n}
                        IP |= {n}
                        c1 = 0
            c2 += 1
            if c2 == g:
                JP |= {i}
                RP |= {i}
                c2 = 0
        S -= SP
        I = (I|IP)-JP
        R |= RP
    print(len(R))

# read the edges from the 'com-dblp.ungraph.txt' file
G = nx.read_edgelist('com-dblp.ungraph.txt', create_using=nx.DiGraph(), comments='#')

print('Number of nodes:', len(G.nodes()))
print('Number of edges:', len(G.edges()))

SIRModel_Book(G,{'0'})
SIRModel_Corrected(G,{'0'})