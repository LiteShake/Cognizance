"""
QUESTION 3

What is the result of the following expression ?

print(0 * np.nan)
print(np.nan != np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(0.3 == 3 * 0.1) 
"""

import numpy as np 

print(0 * np.nan)   # ARITHMETIC OPERATIONS ON SOMETHING THATS NOT A NUMBER IS NOT A NUMBER

print(np.nan != np.nan) # TRUE BECAUSE OF THE UNCERTAINITY OF NAN

print(np.inf > np.nan)  # ANY OPERATIONS WITH NAN WON'T WORK BECAUSE OF ITS UNCERTAINITY.
# INFINITY IS ASSUMED TO BE A CERTAIN VALUE THAT IS PROGRAMMED TO BE BIGGER THAN ANY CERTAIN VALUE. 

print(np.nan - np.nan)  # ARITHMETIC OPERATIONS ON SOMETHING THATS NOT A NUMBER IS NOT A NUMBER

print(0.3 == 3 * 0.1)   # BECAUSE 0.3 != 0.30000000000000004 AND BECAUSE OF PYTHON'S 16 DIGIT ACCURACY WHEN DEALING WITH FLOATS