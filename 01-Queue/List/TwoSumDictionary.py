

'''
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Ref: https://www.javatpoint.com/python-solution-of-two-sum-problem-of-given-list

Space Complexity
Using the dictionary, it takes only one for loop so the time complexity will be the O(N).
'''
from numpy import number

class TwoSum:
    def twoSum(self, nums, target):
        # declaring a dictionary to keep track of all the values
        visited_numbers = dict()

        # iterating over the entire array
        for index, num in enumerate(nums):

            # subtracting the num from the target to search for its pair
            number_to_be_search = target - num

            #  if the pair is found, return the index of the both numbers
            if number_to_be_search in visited_numbers:
                return [index, visited_numbers[number_to_be_search]]
            else:
                visited_numbers[num] = index

list1 = [2, 7, 11, 15]      
target = 18  
obj = TwoSum()  
print(obj.twoSum(list1, target))  