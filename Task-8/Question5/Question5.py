"""
QUESTION 5

Do any two Exercises using Numpy

1.addition of 2 numpy arrays
2.Multiplying a matrix
3.Identity Matrix
4.Array datatype conversion
5.Array re-dimensioning
6.Custom Sequence Generation
7.Getting the positions (indexes) where elements of 2 numpy arrays match
"""

import numpy as np

"""
2 : MATRIX MULTIPLICATION
"""
print("MATRIX MULTIPLICATION\n")

A = np.random.randint(4, 7, (3,5))
B = np.random.randint(4, 7, (5,3))

print(f"\nA = \n{A}")
print(f"\nB = \n{B}")

C = np.matmul( A, B )
print(f"\nC = A x B = \n{C}")



"""
7 : INDICES WHERE 2 NP-ARRAYS HAVE MATCH
"""

print("\nINDICES WHERE 2 NP-ARRAYS HAVE MATCH\n")

def GetCommonIndices( M1, M2 ) :

    small = None
    if( len(M1) > len(M2) ) : small = M2     # FINDING SMALL ARRAY IN CASE OF DIFFERENT LENGTHS TO ITERATE LESS
    else : small = M1                        # POINTLESS IN THIS CASE BECAUSE BOTH ARE OF SAME LENGTH
    
    indices = []                             # LIST FOR COMMON INDICES
    for i in range( len( small ) ) :
        if( X[i] == Y[i]) :                  # CONDITION TO CHECK EQUALITY
            indices.append(i)
            
    return indices

X = np.random.randint(0, 9, 19)
Y = np.random.randint(0, 9, 19)
print(f"Indices where {X} and {Y} have same element" )
print( GetCommonIndices(X,Y) )
