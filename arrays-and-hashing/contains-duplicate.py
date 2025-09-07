'''
||| PROBLEM|||

Given an integer array nums, 
return true if any value appears at least twice in the array, 
and return false if every element is distinct.

||| SOLUTION |||
'''
from types import List

def containsDuplicate(self, nums: List[int]) -> bool:
    # set of nums to store unique nums
    numset = set()

    # loop through nums and if current num already in numset, return True for
    # containing duplicate, else add num to numset. If nums fully looped through, return False.
    for num in nums:
        if num in numset:
            return True
        numset.add(num)

    return False

'''
n: len(nums)

Time Complexity: O(n) [single non-nested for loop]

Space Complexity: O(n) [len(numset) <= n]
'''