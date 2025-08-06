# You are given an integer array nums and an integer val. Your task is to remove all occurrences of val from nums in-place.
# After removing all occurrences of val, return the number of remaining elements, say k, such that the first k elements of nums do not contain val.
# Note:
# The order of the elements which are not equal to val does not matter.
# It is not necessary to consider elements beyond the first k positions of the array.
# To be accepted, the first k elements of nums must contain only elements not equal to val.
# Return k as the final result.
# Example :
# Input: nums = [1,1,2,3,4], val = 1
# Output: [2,3,4]

# Method 1: (Brute Force)
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        tmp = []
        for num in nums:
            if num == val:
                continue
            tmp.append(num)
        
        for i in range(len(tmp)):
            nums[i] = tmp[i]

        return len(tmp)    

# Method 2: (Two Pointers)
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if  nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k