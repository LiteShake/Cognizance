"""
QUESTION 1

Consider the vector [10, 11, 12, 13, 14], how to build a new vector 
with 5 consecutive zeros interleaved between each value?

In :
First Number: 10
Last Number: 14

Out :
[10.  0.  0.  0.  0.  0. 11.  0.  0.  0.  0.  0. 12.  0.  0.  0.  0.  0. 13.  0.  0.  0.  0.  0. 14.]
"""

import numpy as np

def Problem(fnum , lnum) :
    out = np.concatenate( (np.array([fnum]), np.zeros(shape=5) ))

    for i in range(fnum + 1, lnum):
        
        out = np.concatenate( (out, np.concatenate( (np.array([i]) , np.zeros(shape=5) ))) )
    
    out = np.concatenate( (out, np.array([lnum]) ))

    return out

a = int( input("Enter first number : ") )
b = int( input("Enter last number : ") )

print( Problem(a,b) )
