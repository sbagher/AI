import numpy as np

a=np.empty(3,dtype=object)
a[0]=[]
a[1]=[]
a[2]=[]

a[1].append(1)
a[1].append(2)
a[1].append(3)
a[0].append(0)
a[2].append(5)

print (5 in a[3])