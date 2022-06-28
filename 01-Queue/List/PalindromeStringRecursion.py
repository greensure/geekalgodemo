
'''
9. Palindrome Number

Ref: https://www.knowprogram.com/python/palindrome-string-python/

Palindrome String in Python 

If the reverse of the string is the same string then the string is called palindrome string. 
Some examples of palindromic words are redivider, noon, civic, radar, level, rotor, kayak, 
reviver, racecar, redder, madam, and refer. 
The palindrome number is also based on the palindrome string. 
The reverse of a number that is equal to the same number is called a palindrome number.
'''

from sqlalchemy import true

def isPalindrome(s):
    s = s.lower()
    length = len(s)

    if length < 2:
        return true

    elif s[0] == s[length - 1]:
        # Call is pallindrome form substring(1, length - 1) 
        return isPalindrome(s[1: length - 1])
    else:
        return False

# take inputs
string = input('Enter the string: ')

# calling function and display result
reverse = isPalindrome(string)

if reverse:
    print(string, 'is a Palindrome')
else:
    print(string, 'is not a Palindrome')
