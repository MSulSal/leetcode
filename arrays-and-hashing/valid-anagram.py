'''
PROBLEM:

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

SOLUTION:
'''

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    character_counts = [0] * 26

    for i in range(len(s)):
        character_counts[ord(s[i]) - ord("a")] += 1
        character_counts[ord(t[i]) - ord("a")] -= 1

    for count in character_counts:
        if count != 0:
            return False
        
    return True

'''

Time Complexity: O(n) [two non-nested for loops]
Space Complexity: O(1) [len(character_counts) == 26]
'''