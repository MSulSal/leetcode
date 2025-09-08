'''
PROBLEM:

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

SOLUTION:
'''

from typing import List

def productExceptSelf(self, nums: List[int]) -> List[int]:
    products = [1] * len(nums)
    product = 1

    for i in range(len(nums)):
        products[i] *= product
        product *= nums[i]

    product = 1

    for i in range(len(nums) - 1, -1, -1):
        products[i] *= product
        product *= nums[i]

    return products

'''
n: len(nums)
TC: O(n)
SC: O(n)
'''