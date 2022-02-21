"""
Write a python program to make a 2-dimensional list that contains represents a table of records,
for instance, student details like Roll no, Student Name, Marks
"""

# INITIALIZING ARRAY
from audioop import add

from numpy import array


data2D = [
    ["Item No","Name","Price"]
]

# FUNCTION TO PRINT 1D ARRAY
def Print1DArray( list1d ) :
    for elemt in list1d :
        print( str(elemt) + "        " , end = "")  

# FUNCTION TO PRINT 2D ARRAY
def Print2DArray( list2d ) :

    for elemt in list2d[0] :
        print( elemt + "     ", end = " ")
    print()

    for list1d in list2d[1:] :
        Print1DArray( list1d )
        print()


"""
i) Add some records in the list and print the list in tabular form,
"""
# ADDING REQUIRED ELEMENTS TO ARRAY
def AddToArray() :
    
    try :       # ANTI-CRASH IF USER GIVES STRING IN INT / FLOAT FIELDS
        item_no = int(input("\nEnter item no : "))

        if ( item_no == -1 ) : return False     # BREAKS LOOP IF item_no IS -1

        item_name = input("Enter name : ")
        price = float(input("Enter price : "))
        print()

        data2D.append( [item_no, item_name, price] )
        
        Print2DArray(data2D)
        return True
    
    except :
        return True

"""
ii) From created list, extract and print second record/row that contains
"""
def PrintSecondRow() :
    print()
    print("Data at 2'nd Row")
    Print1DArray( data2D[2] )

# START HERE
Print2DArray(data2D)

arrayAdd = True
while( arrayAdd ) : arrayAdd = AddToArray()     # ASK THE USER DATA UNTIL RETURN VALUE IS FALSE

PrintSecondRow()

