"""
Write a program to check if the given number is a palindrome number.
"""

def FindNumOfDigs( test_num ) :
    num_digits = 0      # INITIALISES NUMBER OF DIGITS TO 0
                                # ASSUME NUMBER BE "abcde"
    while ( test_num >= 1 ) :   # ITERATIONS  : 0       1      2       3       4       5
        num_digits += 1         # DIGIT COUNT : 0       1      2       3       4       5
        test_num //= 10         # NUMBER      : abcde   abcd   abc     ab      a       <loop breaks>  
    
    return num_digits           # RETURNS NUMBER OF DIGITS


def CheckPalindrome( check_num ) :      # FUNCTION TO CHECK PALINDROME
    new_num = 0                 # INITIALIZES REVERSE NUMBER TO ZERO
    orig_num = check_num        # BACKS UP ORIGINAL NUMBER BECAUSE ITS GONNA GO THROUGH A LOT OF MATH

    numOfDigits = FindNumOfDigs(check_num)      # FINDS NUMBER OF DIGITS OF THE GIVEN NUMBER

    while ( check_num >= 1 ) :                                          # ITERATIONS    :   1       2       3       4       5
                                                            
        new_num += ( check_num % 10 ) * ( 10 ** (numOfDigits - 1) )     # new_num       :   e0000   ed000   edc00   edcb0   edcba
        check_num //= 10                                                # check_num     :   abcd    abc     ab      a       <loop breaks>

        numOfDigits -= 1                                                # numOfDigits   :   5       4       3       2       1
    
    if( orig_num == new_num ) : return True         # CHECKS IF GIVEN NUMBER IS EQUAL TO REVERSE OR NOT
    else : return False

# START HERE
print( CheckPalindrome( int(input("Enter a number to be checked if Palindrome : ")) ) )     # GETS INPUT, CHECKS PALINDROME , PRINTS RESULT
