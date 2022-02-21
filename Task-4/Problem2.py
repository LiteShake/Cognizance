"""
Write a program to accept a string from the user and display characters, that are
present at an even index number.
"""
"""
Quick Intro :

I tried to get even characters of a string without using indices 
I creates a control variable that is true for every even iteration and false for every odd iteration
So if the control variable is true the character gets added to the new word.
"""

# FUNCTION TO RETURN EVEN CHARACTER WORDS
def EvenChars( word ) :     # INPUTS WORD
    
    even_word = ""          # CREATES EMPTY STRING
    char_control = True     # CREATED A VARIABLE TO KEEP TRACK OF INDICES
    
    for character in word : # LOOP THROUGH THE WORD

        # IF CHARACTER VARIBLE IS TRUE (WHICH IS ONLY IN EVEN INDICES) ADD THE CHARACTER TO NEW WORD
        if (char_control) : even_word += character   
        char_control = not char_control     # INVERTS CHARACTER VARIABLE

    return even_word    # RETURN THE NEW WORD

print( EvenChars( input("Enter the string : ") ) )      # INPUTS STRING FROM USER AND PRINTS THE RESULT FROM THE FUNCTION
