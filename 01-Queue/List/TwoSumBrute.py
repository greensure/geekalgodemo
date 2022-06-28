

'''
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''

'''
Brute Force Approach

In this approach, our primary goal is to solve the problem, not efficiently. 
We check every possible pair and the number of possible pairs in the array. 
We will use the two for loop, add the two values, and compare the target value. 
If it is equal to the target value, return the indices of pairs of the integer.

Time Complexity of Two Number Sums (Brute Force Approach)
We need to use the two for loops. The first for loop visits n numbers of elements and second for loop visits n-1. 
Hence, the check for the possible and total number of pair are: N*(N-1)/2, the time-complexity will be O(N*N) = N^2.

Space Complexity
0(1): Only constant space for variable is used.

'''
class TwoSum:
    def __init__(self, list1, target):
        self.list1 = list1
        self.target = target

    def solution(self):
        length = len(list1)

        for i in range(length - 1):
            for j in range(i + 1, length):
                if list1[i] + list1[j] == self.target:
                    new_list = i, j
                    return list(new_list)
        return -1

list1 = [1, 2, 4, 5, 11]  
target = 6  
obj = TwoSum(list1, target)  
print(obj.solution())          

