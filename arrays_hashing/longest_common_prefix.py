# You are given an array of strings strs. Return the longest common prefix of all the strings.
# If there is no longest common prefix, return an empty string "".
# Example 1:
# Input: strs = ["bat","bag","bank","band"]
# Output: "ba"
# Example 2:
# Input: strs = ["dance","dag","danger","damage"]
# Output: "da"
# Example 3:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

from typing import List

class Solution1:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        longest_common_prefix = ""

        sorted_list = sorted(strs)

        first = sorted_list[0]
        last = sorted_list[-1]

        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                longest_common_prefix += first[i]
            else:
                break
        return longest_common_prefix

print(Solution1().longestCommonPrefix(["bat","bag","bank","band"]))
print(Solution1().longestCommonPrefix(["dance","dag","danger","damage"]))
print(Solution1().longestCommonPrefix(["dog","racecar","car"]))

class Solution2:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        base = strs[0]

        for i in range(len(base)):
            for s in strs[1:]:
                if i == len(s) or s[i] != base[i]:
                    return base[0:i]

        return base

print(Solution2().longestCommonPrefix(["bat","bag","bank","band"]))
print(Solution2().longestCommonPrefix(["dance","dag","danger","damage"]))
print(Solution2().longestCommonPrefix(["dog","racecar","car"]))