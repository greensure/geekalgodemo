'''
9. Palindrome Number

Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is a palindrome while 123 is not.

Ref: https://www.edureka.co/blog/python-program-to-check-palindrome/

This is one of the easiest programs to find Palindrome program using while loop
'''

num = int(input("Enter a number: "))
temp = num
rev = 0
while(num > 0):
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10
if(temp == rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")