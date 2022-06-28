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

# take inputs
string = input('Enter the string: ')

# find reverse of string
i = string
reverse = ''
while(len(i) > 0):
    if(len(i) > 0):
        a = i[-1]
        i = i[:-1]
        reverse += a

# compare reverse to original string
if(reverse == string):
    print(string, 'is a Palindrome')
else:
    print(string, 'is not a Palindrome')
