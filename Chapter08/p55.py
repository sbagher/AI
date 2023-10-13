# Name: Saeed Baghershahi
# Student Number: 102501002
# Class: AI Applications in Social Networks
# Assignment: Problem: 55, Chapter: 08, Book: "Practical Social Network Analysis with Python"


from collections import Counter

print('Problem: 55, Chapter: 08, Book: "Practical Social Network Analysis with Python"\n')
print('For this threshold vector, compute the histogram N.')

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
print (f'N = {N}')