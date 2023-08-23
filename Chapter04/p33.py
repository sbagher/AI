# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 33, Chapter: 04, Book: "Practical Social Network Analysis with Python"
import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter

print('Problem: 33, Chapter: 04, Book: "Practical Social Network Analysis with Python"\n')
print('Degree distribution\n')

# read the edges from the 'CA-AstroPh.txt' file
rwg = nx.read_edgelist('CA-GrQc.txt', create_using=nx.DiGraph(), comments='#')

rwg_nodes = len(rwg.nodes())
rwg_edges = len(rwg.edges())

swg = nx.watts_strogatz_graph(rwg_nodes, 5 , 0.5)

rwg_edges = len(swg.edges())
rwg_nodes = len(swg.nodes())
