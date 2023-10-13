# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 56, Chapter: 08, Book: "Practical Social Network Analysis with Python"

from collections import Counter
import matplotlib.pyplot as plt

print('Problem: 56, Chapter: 08, Book: "Practical Social Network Analysis with Python"\n')
print('Using the N calculated in Problem 55, compute its cumulative histogram [N] =\n\
(N[1], . . . , N[n−1]), where N[k] = k l=0 Nl . Plot the cumulative histogram and report\n\
the final number of rioters.')

T = [1, 1, 1, 1, 1, 4, 1, 0, 4, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 4, 0, 1, 4, 0, 1, 1, 1, 
     4, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 4, 1, 1, 4, 1, 4, 
     0, 1, 0, 1, 1, 1, 0, 4, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 
     1, 0, 4, 0, 4, 0, 0, 1, 1, 1, 4, 0, 4, 0]
C = Counter(T)
#C = sorted(C.items(), key=lambda x: (x[0], x[1]))
N = []
for i in range (max(C.keys())+1):
    if i in C.keys():
        N.append(C[i])
    else:
        N.append(0)

# cumulative
NC = [N[0]]
for i in range (1, max(C.keys())+1):
    NC.append(NC[i-1]+N[i])

print (f'N = {N}')
print (f'[N] = {NC}')
print (f'The ﬁnal number of rioters = {NC[-1]}')

plt.plot(range (max(C.keys())+1), N, color ='green', linewidth=1, label='Number of Rioters')
plt.plot(range (max(C.keys())+1), NC, color ='blue', linewidth=1, label='Cumulative Number of Rioters')
plt.title('(Number of Rioters) and (Cumulative Number of Rioters)')
plt.xlabel('T (threshold)')
plt.ylabel('Number of Rioters')
plt.legend()

plt.show()