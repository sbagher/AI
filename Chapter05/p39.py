# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 39, Chapter: 05, Book: "Practical Social Network Analysis with Python"

import snap
import time

start_time = time.time()

# read the edges from the 'com-friendster.ungraph.txt' file
Graph = snap.LoadEdgeList(snap.PNGraph, "com-friendster.ungraph.txt", 0, 1)

end_time = time.time()
elapsed_time = end_time - start_time

f = open("demofile2.txt", "w")
f.write(elapsed_time)
f.close()

print(elapsed_time)
