"""
Print the following pattern.
    *
   * * 
  * * *
 * * * *
* * * * *
"""



def Pattern( layers ) :     # THIS A FUNCTION

    for layer in range( layers , 0, -1 ) :      # LOOPING IN REVERSE FROM NUMBER OF LAYERS TO 0 
        print( " " * (layer - 1) + "* " * (layers - layer + 1)  )       # PRINTING THE CORRECT AMOUNT OF SPACES AND STARS

Pattern(5)      # CALLING THE FUNCTION
