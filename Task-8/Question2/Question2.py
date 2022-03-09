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

def GetArrays() :

    is_2d = False   # IS THE ARRAY GONNA BE 2D ??

    # GET ARRAY DIMENSIONS FROM USER
    dims = input("Enter dimensions of array as \"X\" for 1d or \"X Y\" for 2d array : ").strip().split()

    is_2d = bool( len(dims) == 2 )  # CHECKS IF ARRAY IS 2D BY LENGTH OF DIMENSIONS

    if( is_2d ) :   

        np_A = np.zeros(shape= ( int(dims[0]), int(dims[1]) ) ) # CREATES A 2D ZERO ARRAY IN USER'S REQUIRED DIMENSIONS
        np_B = np.zeros_like(np_A)                              # CREATES ANOTHER SIMILAR ARRAY FOR B
        print(f"Array A : \n{np_A}" )   # *PRINTS ARRAY*


        for i in range( int(dims[0]) ) :        # DOUBLE LOOP FOR 2D ARRAY TRAVERSAL
            for j in range( int(dims[1]) ) :

                np_A[i,j] = int( input("enter a number : "))    # ASK FOR VALUE
                print(f"Array A : \n{np_A}" )

        print(f"\nArray B : \n{np_B}" )

        for i in range( int(dims[0]) ) :
            for j in range( int(dims[1]) ) :

                np_B[i,j] = int( input("enter a number : "))
                print(f"Array B : \n{np_B}" )
    
    else :
        np_A = np.zeros(shape=int(dims[0]) )    # CREATES A ZERO ARRAY IN USER'S REQUIRED LENGTH
        np_B = np.zeros_like(np_A)
        print(f"Array A : \n{np_A}" )

        for i in range( int(dims[0]) ) :        # LOOP FOR ARRAY TRAVERSAL
                                
            np_A[i] = int( input("enter a number : "))
            print(f"Array A : \n{np_A}" )

        print(f"\nArray B : \n{np_B}" )

        for i in range( int(dims[0]) ) :
                                
            np_B[i] = int( input("enter a number : "))
            print(f"Array B : \n{np_B}" )

    return (np_A, np_B)     # RETURN BOTH ARRAYS 

A, B = GetArrays() # CALLING FUNCTION, UNPACKING RETURN VALUES
print("\n" * 2)    # A BUNCH OF NEW LINES FOR NICE PRESENTATION

print(f"A = \n{A}")
print(f"B = \n{B}")

print(f"Is A == B ? {np.array_equal(A,B)}" )    # np.array.equal() TO CHECK IF TWO ARRAYS ARE EQUAL IN SHAPE AND SIZE
