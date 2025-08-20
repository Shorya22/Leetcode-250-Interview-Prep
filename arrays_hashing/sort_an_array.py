"""
Problem: Sort an Array

You are given an array of integers `nums`. Your task is to sort the array in ascending order and return it.

Requirements:
- You must not use any built-in sorting functions.
- Your solution should run in O(n log n) time complexity.
- Your solution should use the smallest possible space complexity.

Example 1:
Input: nums = [10, 9, 1, 1, 1, 2, 3, 1]
Output: [1, 1, 1, 1, 2, 3, 9, 10]

Example 2:
Input: nums = [5, 10, 2, 1, 3]
Output: [1, 2, 3, 5, 10]

Constraints:
- 1 <= nums.length <= 50,000
- -50,000 <= nums[i] <= 50,000
"""
from typing import List
# Method 1:
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        for i in range(n-1):
            for j in range(n-i-1):

                if nums[j] > nums[j+1]:
                    nums[j] , nums[j+1] = nums[j+1] , nums[j]

        return nums

# Method 2:
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(left, right):
            new = []
            i = 0
            j = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    new.append(left[i])
                    i += 1
                else:
                    new.append(right[j])
                    j += 1

            new.extend(left[i:])
            new.extend(right[j:])
            return new

        def merge_sort(nums: List[int]):
            if len(nums) <= 1:
                return nums
            
            mid = len(nums) // 2
            left_arr = nums[:mid]
            right_arr = nums[mid:]

            left_arr = merge_sort(left_arr)
            right_arr = merge_sort(right_arr)
            return merge(left_arr, right_arr)
        
        return merge_sort(nums)

# Method 3:
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge_sort(nums):

            if len(nums) == 1:
                return nums
            
            mid = len(nums) // 2
            left_arr = nums[:mid]
            right_arr = nums[mid:]

            left_arr = merge_sort(left_arr)
            right_arr = merge_sort(right_arr)

            merge(left_arr,right_arr,nums)
            return nums

        def merge(left,right,nums):
            i = 0
            j = 0
            k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1

                k +=1

            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1
            
            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1
            
        return merge_sort(nums)