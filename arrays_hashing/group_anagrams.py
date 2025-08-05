# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
# Example :
# Input: strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

from typing import List
from collections import defaultdict

# Method 1: Sorting
class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)
        
        for s in strs:

            sorted_s = "".join(sorted(s))
            res[sorted_s].append(s)
        
        return list(res.values())

# Method 2: Counting
class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for c in word:
                count[ord(c) - ord("a")] += 1

            key = tuple(count)
            res[key].append(word)

        return list(res.values())        