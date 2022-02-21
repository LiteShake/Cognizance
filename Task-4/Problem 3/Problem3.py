"""
Write a python program to make a 2-dimensional list that contains represents a table of records,
for instance, student details like Roll no, Student Name, Marks
"""

data2D = []

"""
i) Add some records in the list and print the list in tabular form,
"""
def Print2DArray( list2d ) :

    for elemt in list2d[0] :
        print( elemt + "   ", end = " ")
    print()

    for list1d in list2d[1:] :

        for elemt in list1d :
            print( str(elemt) + "        ", end = " ")
        print()

def Print1DArray( list1d ) :
    for elemt in list1d :
        print( str(elemt) + "        ", end = " ")  

def AddToArray() :
    
    data2D.append( ["Roll No","Name","Marks"] )
    data2D.append( [1,"Abc",90] )
    data2D.append( [2,"Def",95] )
    data2D.append( [3,"Ghi",85] )
    
    Print2DArray(data2D)

"""
ii) From created list, extract and print second record/row that contains
"""
def PrintSecondRow() :
    print()
    print("Data at 2'nd Row")
    Print1DArray( data2D[2] )

# START HERE
AddToArray()

PrintSecondRow()

