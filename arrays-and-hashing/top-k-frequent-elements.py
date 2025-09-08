'''
PROBLEM:

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

SOLUTION:
'''
from typing import List

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    counts = {}
    frequency_buckets = [[] for _ in range(len(nums) + 1)]

    for num in nums:
        counts[num] = 1 + counts.get(num, 0)

    for num, count in counts.items():
        frequency_buckets[count].append(num)

    top_k = []

    for i in range(len(frequency_buckets) - 1, 0, -1):
        for num in frequency_buckets[i]:
            top_k.append(num)
            if len(top_k) == k:
                return top_k

    return []

'''
n: len(nums)
TC: O(n)
SC: O(n)
'''