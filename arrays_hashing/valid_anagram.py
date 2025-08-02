# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
# Example :
# Input: s = "racecar", t = "carrace"
# Output: true

# Method 1: Using Hashmap
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hashmap_s,hashmap_t = {},{}
        len_s,len_t = len(s),len(t)

        if len_s != len_t:
            return False

        for i in s:
            if i not in hashmap_s:
                hashmap_s[i] = 1
            else:
                hashmap_s[i] += 1

        for j in t:
            if j not in hashmap_t:
                hashmap_t[j] = 1
            else:
                hashmap_t[j] += 1

        return hashmap_s == hashmap_t

print(Solution.isAnagram(Solution,"racecar","carrace"))
print(Solution.isAnagram(Solution,"jar","jam"))


# Method 2: Using Sorting
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        return sorted(s) == sorted(t)

print(Solution.isAnagram(Solution,"racecar","carrace"))
print(Solution.isAnagram(Solution,"jar","jam"))


# Method 3: Using Counter
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

       return Counter(s) == Counter(t)

print(Solution.isAnagram(Solution,"racecar","carrace"))
print(Solution.isAnagram(Solution,"jar","jam"))