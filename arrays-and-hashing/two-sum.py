'''
PROBLEM:

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

SOLUTION:
'''

from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    nums_index = {}
    
    for i in range(len(nums)):
        num = nums[i]
        diff = target - num
        if diff in nums_index:
            return [nums_index[diff], i]
        nums_index[num] = i

    return []

'''
n: len(nums)
Time Complexity: O(n) [single non-nested for loop]
Space Complexity: O(n) [len(nums_index.items()) <= len(nums)]
'''