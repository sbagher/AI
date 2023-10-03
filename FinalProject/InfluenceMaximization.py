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

def celf_edges_weight(g, k, p=0.1, mc=1000):  
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
    marg_gain = []
    for node in range(nx.number_of_nodes(g)):
        _, tmp = IndependentCascadingModel(g,[node],p,mc)
        tmp = [tmp]
        marg_gain += tmp

    # Create the sorted list of nodes and their marginal gain 
    Q = sorted(zip(range(nx.number_of_nodes(g)),marg_gain), key=lambda x: x[1],reverse=True)

    # Select the first node and remove from candidate list
    S, spread, SPREAD = [Q[0][0]], Q[0][1], [Q[0][1]]
    Q, LOOKUPS = Q[1:], [nx.number_of_nodes(g)]
    
    # ---- Step 2: Find the next k-1 nodes using the list-sorting procedure
    
    for _ in range(k-1):    

        check, node_lookup = False, 0
        
        while not check:
            
            # Count the number of times the spread is computed
            node_lookup += 1
            
            # Recalculate spread of top node
            current = Q[0][0]
            
            # Evaluate the spread function and store the marginal gain in the list
            _, tmp = IndependentCascadingModel(g,S+[current],p,mc)
            tmp = [tmp]
            Q[0] = (current, tmp - spread)

            # Re-sort the list
            Q = sorted(Q, key = lambda x: x[1], reverse = True)

            # Check if previous top node stayed on top after the sort
            check = (Q[0][0] == current)

        # Select the next node
        spread += Q[0][1]
        S.append(Q[0][0])
        SPREAD.append(spread)
        LOOKUPS.append(node_lookup)

        # Remove the selected node from the list
        Q = Q[1:]

    return(S,SPREAD,LOOKUPS)

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
    marg_gain = []
    for node in range(nx.number_of_nodes(g)):
        tmp, _ = IndependentCascadingModel(g,[node],p,mc)
        tmp = [tmp]
        marg_gain += tmp

    # Create the sorted list of nodes and their marginal gain 
    Q = sorted(zip(range(nx.number_of_nodes(g)),marg_gain), key=lambda x: x[1],reverse=True)

    # Select the first node and remove from candidate list
    S, spread, SPREAD = [Q[0][0]], Q[0][1], [Q[0][1]]
    Q, LOOKUPS = Q[1:], [nx.number_of_nodes(g)]
    
    # ---- Step 2: Find the next k-1 nodes using the list-sorting procedure
    
    for _ in range(k-1):    

        check, node_lookup = False, 0
        
        while not check:
            
            # Count the number of times the spread is computed
            node_lookup += 1
            
            # Recalculate spread of top node
            current = Q[0][0]
            
            # Evaluate the spread function and store the marginal gain in the list
            tmp, _ = IndependentCascadingModel(g,S+[current],p,mc)
            tmp = [tmp]
            Q[0] = (current, tmp - spread)

            # Re-sort the list
            Q = sorted(Q, key = lambda x: x[1], reverse = True)

            # Check if previous top node stayed on top after the sort
            check = (Q[0][0] == current)

        # Select the next node
        spread += Q[0][1]
        S.append(Q[0][0])
        SPREAD.append(spread)
        LOOKUPS.append(node_lookup)

        # Remove the selected node from the list
        Q = Q[1:]

    return(S,SPREAD,LOOKUPS)


G = CreateGraph()

output_greedy_nodes_count, sgn  = greedy_nodes_count (G, 10, p = 0.1, mc = 1000)
output_celf_nodes_count, scn, _ = celf_nodes_count   (G, 10, p = 0.1, mc = 1000)

# Print resulting seed sets
print("Algorith 1: Maximizing Number of Nodes:")
print("optimal seed set with greedy : " + str(output_greedy_nodes_count))
print("optimal seed set with celf   : " + str(output_celf_nodes_count))

output_greedy_edges_weight, sge  = greedy_edges_weight (G, 10, p = 0.1, mc = 1000)
output_celf_edges_weight, sce, _ = celf_edges_weight   (G, 10, p = 0.1, mc = 1000)

# Print resulting seed sets
print("\nAlgorith 2: Maximizing Sum of Influence Weights:")
print("optimal seed set with greedy : " + str(output_greedy_edges_weight))
print("optimal seed set with celf   : " + str(output_celf_edges_weight))