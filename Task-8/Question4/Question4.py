"""
QUESTION 4

Convert the first character of each element in a series to uppercase?

In :
ser = pd.Series(['amrita', 'school', 'of', 'engineering' 'chennai' , 'campus'])

Out :
Amrita School Of Engineering Chennai Campus
"""

import pandas as pd

ser = pd.Series(["amrita","school","of","engineering","chennai","campus"])


def CapitalizeFirst() :
    global ser

    for i in range( len(ser) ) :    # TRAVERSING THROUGHT THE ARRAY
        ser[i] = ser[i].capitalize()    # CAPITALIZING AND ASSIGNING AN ELEMENT TO ITSELF


print("Before :\n" , ser )
CapitalizeFirst()
print("After :\n" , ser )
