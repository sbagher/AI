# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Final Project (Influence Maximization), Book: "Practical Social Network Analysis with Python"

"""
Description:
   Diffusion Model: Independent Cascading Model
   Maximization Algorithm: celf++
   Graph: directed Erdös–Rényi graph (n=500)
   k: 10
   Objective: Influence Maximization for 10 optimal seed set
"""

import networkx as nx
import random
import ndlib
import ndlib.models.epidemics as ep
import ndlib.models.ModelConfig as mc
import statistics as s
from time import time

def CreateGraph(n, k, p, beta=None):
   # n The number of nodes
   # k Each node is joined with its k nearest neighbors in a ring topology.
   # p The probability of rewiring each edge

   g = nx.connected_watts_strogatz_graph(n, k, p)
   while nx.is_connected(g) == False:
      g = nx.connected_watts_strogatz_graph(n,k, p)    

   config = mc.Configuration()

   for a, b in g.edges():
      if beta:
         weight = beta
      else:
         weight = random.randrange(40,80)
         weight = round(weight / 100, 2)
         
      g[a][b]['weight'] = weight
      config.add_edge_configuration("threshold", (a, b), weight)

   return g, config

def IndependentCascadingModel (g, config, seed, rounds=100):
   result = []

   for iter in range(rounds):

      model_temp = ep.IndependentCascadesModel(g) # _temp
      config_temp = mc.Configuration()
      config_temp.add_model_initial_configuration('Infected', seed)

      for a, b in g.edges(): # _temp
         weight = config.config["edges"]['threshold'][(a, b)]
         # g_temp[a][b]['weight'] = weight
         config_temp.add_edge_configuration('threshold', (a, b), weight)

      model_temp.set_initial_status(config_temp)

      iterations = model_temp.iteration_bunch(5)

      total_no = 0

      for j in range(5):
         a = iterations[j]['node_count'][1]
         total_no += a

      result.append(total_no)

   return result

def celfpp(g, config, budget, rounds=100):

   # Compute marginal gain for each node
   candidates = list(g.nodes())
   marg_gain = [s.mean(IndependentCascadingModel(g, config, [node], rounds)) for node in candidates]

   # Create the sorted list of nodes and their marginal gain 
   Q = sorted(zip(candidates, marg_gain), key = lambda x: x[1], reverse=True)

   # Select the first node and remove from candidate list
   selected, spread, Q = [Q[0][0]], Q[0][1], Q[1:]

   # Initialize last_seed as the first selected node
   last_seed = selected[0]
   
   # Find the next budget-1 nodes using the CELF++ procedure
   for _ in range(budget - 1):    
         check = False
         while not check:
            # Get current node and its previous computed marginal gain
            current, old_gain = Q[0][0], Q[0][1]

            # Check if the last added seed has changed
            if current != last_seed:
               # Compute new marginal gain
               new_gain = s.mean(IndependentCascadingModel(g, config, selected+[current], rounds)) - spread
            else:
               # If the last added seed hasn't changed, the marginal gain remains the same
               new_gain = old_gain

            # Update the marginal gain of the current node
            Q[0] = (current, new_gain)

            # Re-sort the list
            Q = sorted(Q, key = lambda x: x[1], reverse=True)

            # Check if previous top node stayed on top after the sort
            check = Q[0][0] == current

         # Select the next node
         selected.append(Q[0][0])
         spread += Q[0][1]  # Update the spread
         last_seed = Q[0][0]  # Update the last added seed

         # Remove the selected node from the list
         Q = Q[1:]

   print(selected)
   return selected

def effect(g, config, result):

   input = []

   for i in range(1000):

      g_mid = g.__class__()
      g_mid.add_nodes_from(g)
      g_mid.add_edges_from(g.edges)

      model_mid = ep.IndependentCascadesModel(g_mid)
      config_mid = mc.Configuration()
      config_mid.add_model_initial_configuration('Infected', result)

      for a, b in g_mid.edges():
         weight = config.config["edges"]['threshold'][(a, b)]
         g_mid[a][b]['weight'] = weight
         config_mid.add_edge_configuration('threshold', (a, b), weight)

      model_mid.set_initial_status(config_mid)

      iterations = model_mid.iteration_bunch(5)
      trends = model_mid.build_trends(iterations)

      total_no = 0

      for j in range(5):
         a = iterations[j]['node_count'][1]
         total_no += a

      input.append(total_no)

   e = s.mean(input)
   v = s.stdev(input)

   return e,v

g, config = CreateGraph(300, 10, 0.1)
print('------------------------------------------------')
print('celfpp')
start = time()
set = celfpp(g, config, 5, rounds=10)
end = time()
print('time: ', end - start)
ie,var = effect(g, config, set)
print('IE:', ie, " +_ ", var)
