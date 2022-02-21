"""
Print the following pattern.
    *
   * * 
  * * *
 * * * *
* * * * *
"""
"""
Quick intro :

After seeing the pattern I saw that the number of  stars are increasing according to the layer number and 
the number of spaces are decreasing from (layer number - 1) to 0.
So I put that thing in a for loop and multiplied the string to get repeated string accordingly,
concatenated and printed one by one.
"""


def Pattern( layers ) :     # THIS A FUNCTION

    for layer in range( layers , 0, -1 ) :      # LOOPING IN REVERSE FROM NUMBER OF LAYERS TO 0 
        print( " " * (layer - 1) + "* " * (layers - layer + 1)  )       # PRINTING THE CORRECT AMOUNT OF SPACES AND STARS

Pattern(5)      # CALLING THE FUNCTION
