"""
Write a program to check if the given number is a palindrome number.
"""

def FindNumOfDigs( test_num ) :
    num_digits = 0

    while ( test_num >= 1 ) :
        num_digits += 1
        test_num //= 10
    
    return num_digits


def CheckPalindrome( check_num ) :
    new_num = 0
    orig_num = check_num
    numOfDigits = FindNumOfDigs(check_num)

    while ( check_num >= 1 ) :
        
        new_num += ( check_num % 10 ) * ( 10 ** (numOfDigits - 1) )
        check_num //= 10

        numOfDigits -= 1
    
    if( orig_num == new_num ) : return True
    else : return False

print( CheckPalindrome( int(input("Enter a number to be checked if Palindrome : ")) ) )
