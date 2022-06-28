'''
9. Palindrome Number

Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is a palindrome while 123 is not.

Ref: https://www.edureka.co/blog/python-program-to-check-palindrome/

Explanation: 
In the above program, first take input from the user (using input OR raw_input() method) to check for palindrome. 
Then using slice operation [start:end:step], check whether the string is reversed or not. 
Here, step value of -1 reverses a string. 
If yes, it prints a palindrome else, not a palindrome.
'''

string = input(("Enter a string: "))
if(string == string[::-1]):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")