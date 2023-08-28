import numpy as np
import random

def h (v,u):
    if u == v:
        return 0
    t = 1023
    for i in range(1,11,1):
        t = t<<1
        if (v & t)==(u & t):
            return i

def normalize(a):
    p = np.zeros(11, dtype=np.float64)
    for i in range(1,11,1):
        p[i] = 2 ** (-a*i)

    wpz1 = np.zeros(1000, dtype=np.float64)
    wpz2 = np.zeros(1000, dtype=np.float64)
    for n1 in range(0,1000,1):
        wp = 0
        for n2 in range(0,1000,1):
            wp += p[h(n1,n2)]
        wpz1[n1] = wp

    f = 1 / max (wpz1)
    for i in range(1,11,1):
        p[i] *= f
    wpz = np.zeros(1000, dtype=np.float64)
    for n1 in range(0,1000,1):
        wp = 0
        for n2 in range(0,1000,1):
            wp += p[h(n1,n2)]
        wpz2[n1] = wp
    print (a,max (wpz1), max (wpz2))
    return p, wpz
for aa in np.arange (0.1, 10.1, 0.1):
    a = round(aa,1)
    normalize(a)
