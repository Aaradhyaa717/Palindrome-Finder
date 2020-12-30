def palindrome_finder(string):
    
    '''
    This function checks if a given string is a palindrome or not.
    
    
    Example:
    Word
    Radar               Palindrome
    Bat                 Not a palindrome
    
    
    '''

    string_lowercase = string.lower()
    #this will makesure there is no confusion in upper and lower case of same letter.
    
    
    
    string_reversed= string_lowercase[::-1]
    
    if string_lowercase == string_reversed:
        return("Yes!" + string +" is a palindrome.")
    else:
        return("Opps!"+ string + " is not a palindrome. Try again!")
    return(string)    
        
print(palindrome_finder("47")) 
print(palindrome_finder("Civic"))

    
