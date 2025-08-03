# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
# Return the answer with the smaller index first.
# Example :
# Input: 
# nums = [3,4,5,6], target = 7
# Output: [0,1]

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}

        for i , n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff],i]
            else:
                hashmap[n] = i

print(Solution().twoSum([3,4,5,6],7))