"""
Print the following pattern.
    *
   * * 
  * * *
 * * * *
* * * * *
"""

def Pattern( layer ) :
    
    total = layer

    for layer in range( layer , 0, -1 ) :
        print( " " * (layer - 1) + "* " * (total - layer + 1)  )

Pattern(5)
