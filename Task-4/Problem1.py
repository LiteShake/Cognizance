"""
Write a program to perform addition on two user input numbers
"""

# I CREATED A SUM FUNCTION BECAUSE WHY NOT ?
def Sum(fst_num , sec_num) :    # INPUTS TWO NUMS
    return fst_num + sec_num    # RETURNS SUM

fs_num = int(input("First number : "))   # INPUT FIRST NUMBER 
se_num = int(input("Second Number : "))  # INPUT SECOND NUMBER

print( "Sum =", Sum(fs_num , se_num) )     # PRINTS SUM
