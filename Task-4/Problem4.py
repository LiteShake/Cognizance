"""
Write a program to check if the given number is a palindrome number.
"""
"""
Quick Intro :

I could've easily converted the int to string and reversed it by slicing [::-1] and converted back to int
and I could've appended all the digits to a list, and run a reverse loop through it and added the digits.

So I tried to make a method to use only one datatype "int" all over the program. No lists or strings.

Although I tried to make the program as efficient as possible I'd strongly recommend using the above two methods for maximum efficiency.
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
