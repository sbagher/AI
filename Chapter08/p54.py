# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 54, Chapter: 08, Book: "Practical Social Network Analysis with Python"

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

print('Problem: 54, Chapter: 08, Book: "Practical Social Network Analysis with Python"\n')
print('Simulate the effect of the high roller dinner on the two graphs. First, read in\n\
the graphs and assign the initial configuration as before. Now, before the decision\n\
process, you spend Rs. k on the fancy dinner and then go through the decision process\n\
of counting votes.')


def election1(g, graph_type, k):
    c0 = {8,9}
    c1 = {0,2,4,6}
    c2 = {1,3,5,7}
    v = np.zeros(10000, dtype=int)
    for i in range(10000):
        t = i % 10
        if t in c1:
            v[i] = 1
        elif t in c2:
            v[i] = 2
    # Spending money for voters
    for i in range(3000, 3000+k*10):
        v[i] = 1
    for _ in range (10):
        v3 = 1
        for n in sorted(g.nodes()):
            # Spending money for voters
            if n >= 3000 and n < (3000+k*10):
                continue
            t = n % 10
            if t in c0:
                v1 , v2 = 0, 0
                for nbr in g.neighbors(n):
                    if v[int(nbr)] == 1:
                        v1 += 1
                    elif v[int(nbr)] == 2:
                        v2 += 1
                if v1 > v2:
                    v[int(n)] = 1
                elif v1 < v2:
                    v[int(n)] = 2
                else:
                    v[int(n)] = v3
                    if v3 == 1:
                        v3 = 2
                    else:
                        v3 = 1
            else:
                continue

    v1 , v2 = 0, 0
    for i in range(10000):
        if v[i] == 1:
            v1 += 1
        else:
            v2 += 1

    print (f'\nFor {graph_type}:')
    print (f'-----<< Election Type 1 >>--------')
    if v1 > v2:
        print ("Winner: You")
        print (f"Your Votes:{v1}")
        print (f"Rival Votes:{v2}")
        print (f"Difference:{v1-v2}")
    else:
        print ("Winner: Rival")
        print (f"Your Votes:{v1}")
        print (f"Rival Votes:{v2}")
        print (f"Difference:{v2-v1}")

    return v1, v2

def election2(g, graph_type, k):
    c0 = {8,9}
    c1 = {0,2,4,6}
    c2 = {1,3,5,7}
    v = np.zeros((2,10000), dtype=int)
    for i in range(10000):
        t = i % 10
        if t in c1:
            v[0][i] = 1
            v[1][i] = 1
        elif t in c2:
            v[0][i] = 2
            v[1][i] = 2

    # Spending money for voters
    for i in range(3000, 3000+k*10):
        v[0][i] = 1
        v[1][i] = 1

    ci = 0 # current_itteration
    ni = 1 # next_itteration
    for _ in range (10):
        v3 = 1
        for n in sorted(g.nodes()):
            # Spending money for voters
            if n >= 3000 and n < (3000+k*10):
                continue
            t = n % 10
            if t in c0:
                v1, v2 = 0, 0
                for nbr in g.neighbors(n):
                    if v[ci][int(nbr)] == 1:
                        v1 += 1
                    elif v[ci][int(nbr)] == 2:
                        v2 += 1
                if v1 > v2:
                    v[ni][int(n)] = 1
                elif v1 < v2:
                    v[ni][int(n)] = 2
                else:
                    v[ni][int(n)] = v3
                    if v3 == 1:
                        v3 = 2
                    else:
                        v3 = 1
            else:
                continue
        tmp = ci
        ci = ni
        ni = tmp

    v1, v2 = 0, 0
    for i in range(10000):
        if v[ci][i] == 1:
            v1 += 1
        else:
            v2 += 1

    print (f'\nFor {graph_type}:')
    print (f'-----<< Election Type 2 >>--------')
    if v1 > v2:
        print ("Winner: You")
        print (f"Your Votes:{v1}")
        print (f"Rival Votes:{v2}")
        print (f"Difference:{v1-v2}")
    else:
        print ("Winner: Rival")
        print (f"Your Votes:{v1}")
        print (f"Rival Votes:{v2}")
        print (f"Difference:{v2-v1}")

    return v1, v2

g1 = nx.gnm_random_graph(10000, 100000, seed=10, directed=False)
g2 = nx.barabasi_albert_graph(10000,10,10)

e1g1, e1g2, e2g1, e2g2 = [], [], [], []

for k in range (0, 10):
    v1, _ = election1(g1, "Erdös-Rényi Graph", k)
    e1g1.append(v1)
    v1, _ = election1(g2, "Preferential Attachment Graph", k)
    e1g2.append(v1)
    v1, _ = election2(g1, "Erdös-Rényi Graph", k)
    e2g1.append(v1)
    v1, _ = election2(g2, "Preferential Attachment Graph", k)
    e2g2.append(v1)

plt.rcParams["figure.figsize"] = (15,5)
plt.subplot(1, 2, 1)
plt.plot(range (0, 10000, 1000), e1g1, color ='green', linewidth=1, label='Erdös-Rényi Graph')
plt.plot(range (0, 10000, 1000), e1g2, color ='blue', linewidth=1, label='Preferential Attachment Graph')
plt.title('Election Type 1')
plt.xlabel('K (the amount you spend)')
plt.ylabel('number of votes you win')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(range (0, 10000, 1000), e2g1, color ='green', linewidth=1, label='Erdös-Rényi Graph')
plt.plot(range (0, 10000, 1000), e2g2, color ='blue', linewidth=1, label='Preferential Attachment Graph')
plt.title('Election Type 2')
plt.xlabel('K (the amount you spend)')
plt.ylabel('number of votes you win')
plt.legend()

plt.show()