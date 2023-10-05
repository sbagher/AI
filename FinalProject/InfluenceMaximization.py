# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Final Project (Influence Maximization), Book: "Practical Social Network Analysis with Python"
"""
Description:
   Diffusion Model: Independent Cascading Model
   Maximization Algorithm: greedy & celf
   Graph: directed Erdös–Rényi graph (n=100, m=300)
   k: 10
   Objective: Influence Maximization for 10 optimal seed set
"""

import random
from random import uniform, seed
import numpy as np
import networkx as nx

def CreateGraph():
    g = nx.gnm_random_graph(n=100, m=300, directed=True)

    for a, b in g.edges():
        weight = random.randrange(40,80)
        weight = round(weight / 100, 2)
        g[a][b]['weight'] = weight

    return g

def IndependentCascadingModel(g, S, p=0.5, mc=1000):
    """
    Input:
        g : graph
        S : set of seed nodes
        p : propagation probability
        mc: number of Monte-Carlo simulations
    Output:
        average number of nodes influenced by the seed nodes
    """
    
    # Loop over the Monte-Carlo Simulations
    spread_nodes_count, spread_edges_weight = [], []
    new_edges = set()
    for i in range(mc):
        
        # Simulate propagation process      
        new_active, A = S[:], S[:]
        while new_active:

            # For each newly active node, find its neighbors that become activated
            new_ones, tmp = [], []
            for node in new_active:
                
                # Determine neighbors that become infected
                np.random.seed(i)
                successors = list(g.successors(node))
                success = np.random.uniform(0,1,len(successors)) < p
                tmp = list(np.extract(success, successors))
                new_ones += tmp
                for b in tmp:
                    l = [(int(node), int(b))]
                    new_edges |= set(l)

            new_active = list(set(new_ones) - set(A))
            
            # Add newly activated nodes to the set of activated nodes
            A += new_active

        weight = 0
        for a, b in new_edges:
            weight += g[a][b]['weight']

        spread_nodes_count.append(len(A))
        spread_edges_weight.append(weight)

    return(np.mean(spread_nodes_count), np.mean(spread_edges_weight))

def greedy_edges_weight(g, k, p=0.1, mc=1000):
    """
    Input:
        g : graph
        k : number of seed nodes
        p : propagation probability
        mc: number of Monte-Carlo simulations
    Output:
        optimal seed set
        resulting spread
        time for each iteration
    """

    S, spread = [], []
    
    # Find k nodes with largest marginal gain
    for _ in range(k):

        # Loop over nodes that are not yet in seed set to find biggest marginal gain
        best_spread = 0
        for j in set(range(nx.number_of_nodes(g)))-set(S):

            # Get the spread
            _, s = IndependentCascadingModel(g, S + [j], p, mc)

            # Update the winning node and spread so far
            if s > best_spread:
                best_spread, node = s, j

        # Add the selected node to the seed set
        S.append(node)
        
        # Add estimated spread and elapsed time
        spread.append(best_spread)

    return(S,spread)

def greedy_nodes_count(g, k, p=0.1, mc=1000):
    """
    Input:
        g : graph
        k : number of seed nodes
        p : propagation probability
        mc: number of Monte-Carlo simulations
    Output:
        optimal seed set
        resulting spread
        time for each iteration
    """

    S, spread = [], []
    
    # Find k nodes with largest marginal gain
    for _ in range(k):

        # Loop over nodes that are not yet in seed set to find biggest marginal gain
        best_spread = 0
        for j in set(range(nx.number_of_nodes(g)))-set(S):

            # Get the spread
            s, _ = IndependentCascadingModel(g, S + [j], p, mc)

            # Update the winning node and spread so far
            if s > best_spread:
                best_spread, node = s, j

        # Add the selected node to the seed set
        S.append(node)
        
        # Add estimated spread and elapsed time
        spread.append(best_spread)

    return(S,spread)

def celf_edges_weight (g, k, p=0.1, mc=1000):
    """
    Input:
        g : graph
        k : number of seed nodes
        p : propagation probability
        mc: number of Monte-Carlo simulations
    Output:
        optimal seed set
        resulting spread
        time for each iteration
    """
      
    # ---- Step 1: Find the first node with greedy algorithm ----
    
    # Calculate the first iteration sorted list
    node_count = []
    weight_count = []
    for node in range(nx.number_of_nodes(g)):
        tmp1, tmp2 = IndependentCascadingModel(g,[node],p,mc)
        tmp1 = [tmp1]
        tmp2 = [tmp2]
        node_count += tmp1
        weight_count += tmp2

    # Create the sorted list of nodes and their marginal gain 
    Q = sorted(zip(range(nx.number_of_nodes(g)), node_count, weight_count), key=lambda x: (x[2], x[1]), reverse=True)

    # Select the first node and remove from candidate list
    S, spread = [Q[0][0]], Q[0][2]
    NODE_COUNT = [Q[0][1]]
    WEIGHT_COUNT = [Q[0][2]]
    Q = Q[1:]
    
    # ---- Step 2: Find the next k-1 nodes using the list-sorting procedure
    
    for _ in range(k-1):    

        check = False
        while not check:
            
            # Recalculate spread of top node
            current = Q[0][0]
            
            # Evaluate the spread function and store the marginal gain in the list
            tmp1, tmp2 = IndependentCascadingModel(g,S+[current],p,mc)
            Q[0] = (current, tmp1, tmp2 - spread)

            # Re-sort the list
            Q = sorted(Q, key = lambda x: (x[2], x[1]), reverse = True)

            # Check if previous top node stayed on top after the sort
            check = (Q[0][0] == current)

        # Select the next node
        spread += Q[0][2]
        S.append(Q[0][0])
        NODE_COUNT.append(Q[0][1])
        WEIGHT_COUNT.append(spread)

        # Remove the selected node from the list
        Q = Q[1:]

    return(S, NODE_COUNT, WEIGHT_COUNT)

def celf_nodes_count(g, k, p=0.1, mc=1000):
    """
    Input:
        g : graph
        k : number of seed nodes
        p : propagation probability
        mc: number of Monte-Carlo simulations
    Output:
        optimal seed set
        resulting spread
        time for each iteration
    """
      
    # ---- Step 1: Find the first node with greedy algorithm ----
    
    # Calculate the first iteration sorted list
    node_count = []
    weight_count = []
    for node in range(nx.number_of_nodes(g)):
        tmp1, tmp2 = IndependentCascadingModel(g,[node],p,mc)
        tmp1 = [tmp1]
        tmp2 = [tmp2]
        node_count += tmp1
        weight_count += tmp2

    # Create the sorted list of nodes and their marginal gain 
    Q = sorted(zip(range(nx.number_of_nodes(g)), node_count, weight_count), key=lambda x: (x[1], x[2]), reverse=True)

    # Select the first node and remove from candidate list
    S, spread = [Q[0][0]], Q[0][1]
    NODE_COUNT = [Q[0][1]]
    WEIGHT_COUNT = [Q[0][2]]
    Q = Q[1:]
    
    # ---- Step 2: Find the next k-1 nodes using the list-sorting procedure
    
    for _ in range(k-1):    

        check = False
        while not check:
            
            # Recalculate spread of top node
            current = Q[0][0]
            
            # Evaluate the spread function and store the marginal gain in the list
            tmp1, tmp2 = IndependentCascadingModel(g,S+[current],p,mc)
            Q[0] = (current, tmp1 - spread, tmp2)

            # Re-sort the list
            Q = sorted(Q, key = lambda x: (x[1], x[2]), reverse = True)

            # Check if previous top node stayed on top after the sort
            check = (Q[0][0] == current)

        # Select the next node
        spread += Q[0][1]
        S.append(Q[0][0])
        NODE_COUNT.append(spread)
        WEIGHT_COUNT.append(Q[0][2])

        # Remove the selected node from the list
        Q = Q[1:]

    return(S, NODE_COUNT, WEIGHT_COUNT)

G = CreateGraph()

print("\nAlgorith 1, Maximizing Number of Nodes (All Edges with Same Weights):")
print("---------------------------------------------------------------------")
print("Greedy:")
optimal_seed_set, spread  = greedy_nodes_count (G, 10, p = 0.1, mc = 1000)
print("\tOptimal Seed Set: " + str(optimal_seed_set))
print("\tSpread: " + str(spread))

print("CELF:")
optimal_seed_set, node_count, weight_count = celf_nodes_count (G, 10, p = 0.1, mc = 1000)
print("\tOptimal Seed Set: " + str(optimal_seed_set))
print("\tMean Influenced Nodes: " + str(node_count))
print("\tMean Influence Weight: " + str(weight_count))

print("\nAlgorith 2, Maximizing Sum of Influence Weights (All Edges with Different Weights):")
print("-----------------------------------------------------------------------------------")
print("Greedy:")
optimal_seed_set, spread  = greedy_edges_weight (G, 10, p = 0.1, mc = 1000)
print("\tOptimal Seed Set: " + str(optimal_seed_set))
print("\tSpread: " + str(spread))

print("CELF:")
optimal_seed_set, node_count, weight_count = celf_edges_weight (G, 10, p = 0.1, mc = 1000)
print("\tOptimal Seed Set: " + str(optimal_seed_set))
print("\tMean Influenced Nodes: " + str(node_count))
print("\tMean Influence Weight: " + str(weight_count))
