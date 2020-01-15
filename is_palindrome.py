#PF-Assgn-40
'''Write a recursive function, is_palindrome() to find out whether a string is a palindrome or not. The function should return true, if it is a palindrome. Else it should return false.

Note- Perform case insensitive operations wherever necessary'''

def is_palindrome(word):
    if(len(word)<1):
        return True
    if(word[0]==word[-1]):
        return is_palindrome(word[1:-1])
    elif(word[0].lower()==word[-1]):
        return is_palindrome(word[1:-1])
    elif(word[0].upper()==word[1:-1]):
        return is_palindrome(word[1:-1])
    else:
        return False
#Provide different values for word and test your program
result=is_palindrome("MadAMa")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")
