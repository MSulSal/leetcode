'''
PROBLEM:

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

SOLUTION:
'''

from collections import defaultdict
from typing import List

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    
    for strng in strs:
        char_counts = [0] * 26

        for chr in strng:
            char_counts[ord(chr) - ord("a")] += 1

        groups[tuple(char_counts)].append(strng)

    return list(groups.values())

'''
n: len(strs)
m: len(strng)
TC: O(n * m)
SC: O(n)
'''