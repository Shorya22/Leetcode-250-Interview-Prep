"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times 
in the array. You may assume that the majority element always exists in the array.

Example:
Input: nums = [5, 5, 1, 1, 1, 5, 5]
Output: 5
"""
from typing import List
# Method 1:
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = {}

        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
        for k,v in count.items():
            if v > len(nums) // 2:
                return k

# Method 2:
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        nums = sorted(nums)

        return nums[len(nums)//2]

# Method 3:
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        res = 0
        count = 0

        for n in nums:

            if count == 0:
                res = n
            if n == res:
                count += 1
            else:
                count -= 1
        return res

        



