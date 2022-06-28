'''
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''

'''
In this approach, we will use the binary search algorithm where the given list array must be sorted. 
We need to fix the first index and then the required value to fulfill the target found in the list.

Time Complexity using Two Sum
The time complexity will be O(n) even in the worst case, we visit all the elements in the array only once.

Space complexity
0(1): Only constant space for the variable is used.
Using the dictionary, it takes only one for loop so that the time complexity will be the O(n).
'''

from turtle import left, right

class TwoSum:
    def twoSum(self, list1, target):
        left = 0
        right = len(list1) - 1

        temSum = 0

        while(left < right):
            tempSum = list1[left] + list1[right]
            if tempSum == target:
                return list((left, right))
            elif tempSum > target:
                right -= 1
            elif tempSum < target:
                left += 1
        return list((-1, -1))

list1 = [2, 7, 11, 15]      
target = 26  
obj = TwoSum()  
print(obj.twoSum(list1, target))  