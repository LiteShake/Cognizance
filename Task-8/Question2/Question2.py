"""
QUESTION 2

Consider two random array A anb B, check if they are equal

In :
First array:                                                           
[1 0 0 0 1 0]                                                          
Second array:                                                          
[0 0 1 1 0 1]

Out :
False
"""

import numpy as np

A = np.random.randint(0,2,6)
print(A)

B = np.random.randint(0,2,6)
print(B)

print( (A == B).all() )
