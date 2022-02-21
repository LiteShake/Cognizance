"""
Write a python program to make a 2-dimensional list that contains represents a table of records,
for instance, student details like Roll no, Student Name, Marks
"""


data2D = []

"""
i) Add some records in the list and print the list in tabular form,
"""
def PrintArray( list2d ) :
    for elmt in list2d :
        print( elmt )

def AddToArray() :
    
    data2D.append( ["Roll No","Name","Marks"] )
    data2D.append( [1,"Abc",90] )
    data2D.append( [2,"Def",95] )
    data2D.append( [3,"Ghi",85] )
    
    PrintArray(data2D)

"""
ii) From created list, extract and print second record/row that contains
"""
def PrintSecondRow() :

    print( data2D[2] )


AddToArray()

PrintSecondRow()
