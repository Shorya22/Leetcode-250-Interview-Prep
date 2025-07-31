# Problem 1: Concatenation of Array
# Link: https://neetcode.io/problems/concatenation-of-array?list=neetcode250

# You are given an integer array nums of length n. Create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
# Specifically, ans is the concatenation of two nums arrays.
# Return the array ans.
# Example:
# Input: nums = [1,4,1,2]
# Output: [1,4,1,2,1,4,1,2]

nums = [1,4,1,2]
n = len(nums)

ans = []

def concat_array(nums,x):
    for i in range(0,x):
        for j in nums:
            ans.append(j)
            
    print(ans)
    
concat_array(nums,2)