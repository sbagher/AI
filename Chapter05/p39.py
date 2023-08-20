# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 39, Chapter: 05, Book: "Practical Social Network Analysis with Python"

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import time

start_time = time.time()

# read the edges from the 'com-friendster.ungraph.txt' file
G = nx.read_edgelist('com-friendster.ungraph.txt', create_using=nx.DiGraph(), comments='#')

end_time = time.time()
elapsed_time = end_time - start_time

print(elapsed_time)
