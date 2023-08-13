# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 59, Chapter: 11, Book: "Practical Social Network Analysis with Python"

import networkx as nx
import random

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
    il = [len(I)]
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
        il.append(len(I))
    return len(R), il

def SIRModel_Corrected(G,I):
    b = 20
    g = 2
    c1 = random.choice(range(b))
    c2 = random.choice(range(g))
    S = G.nodes() - I
    R = set()
    il = [len(I)]
    while I:
        SP = set()
        IP = set()
        JP = set()
        RP = set()
        for i in I:
            for n in set(G.successors(i)):
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
        il.append(len(I))
    return len(R), il

# read the edges from the 'com-dblp.ungraph.txt' file
real_world_graph = nx.read_edgelist('com-dblp.ungraph.txt', create_using=nx.DiGraph(), comments='#')

rw_n_nodes = len(real_world_graph.nodes())
rw_n_edges = len(real_world_graph.edges())
ind = [real_world_graph.in_degree(n) for n in nx.nodes(real_world_graph)]
outd = [real_world_graph.out_degree(n) for n in nx.nodes(real_world_graph)]

random_graph = nx.gnm_random_graph(rw_n_nodes,rw_n_edges,seed=10,directed=True)
preferential_attachment_graph = nx.barabasi_albert_graph(rw_n_nodes,4,seed=10)
configuration_graph = nx.directed_configuration_model (ind,outd,seed=10)

def prepare_run_show_result (G,gtype):
    d = [G.degree(n) for n in nx.nodes(G)]
    ds = sorted(d, reverse=True)
    ds = ds[:10]
    highest_degree_nodes = set()
    for n in nx.nodes(G):
        if G.degree(n) in ds:
            highest_degree_nodes |= {n}

    random_nodes = set(random.sample(list(G.nodes()), 10))

    print(f'{gtype} (Nodes: {len(G.nodes())}, Edges: {len(G.edges())})')

    print(f"10 random nodes:")
    for i in random_nodes:
        print(f"Node: {i}, in-degree: {G.in_degree(i)}, out-degree: {G.out_degree(i)}, degree: {G.degree(i)}")

    print(f"Top 10 highest degree nodes:")
    for i in highest_degree_nodes:
        print(f"Node: {i}, in-degree: {G.in_degree(i)}, out-degree: {G.out_degree(i)}, degree: {G.degree(i)}")

    print(f"Total percentage of nodes that became infected with 10 random nodes in each simulation in each graph")

    ir,_ = SIRModel_Book(G, random_nodes)
    ih,_ = SIRModel_Book(G, highest_degree_nodes)
    print(f'{gtype} with 10 nodes (random : {ir/len(G.nodes())*100}, highest degree: {ih/len(G.nodes())*100})')

prepare_run_show_result(real_world_graph,"real world graph")
prepare_run_show_result(random_graph,"random graph")
#prepare_run_show_result(preferential_attachment_graph,"preferential attachment graph")
prepare_run_show_result(configuration_graph,"configuration graph")
