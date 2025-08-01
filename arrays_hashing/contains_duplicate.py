# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
# Example:
# Input: nums = [1, 2, 3, 3]
# Output: true

# method 1: using hashset
def hasDuplicate(nums):
    hashset = set()

    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)
    return False

print(hasDuplicate([1,2,3,4])) # False
print(hasDuplicate([1,1,1,3,3,4,3,2,4,2])) # True
print(hasDuplicate([1,2,3,1])) # True

# method 2: using hashmap
def check_duplicate(nums):
    seen = {}
    for i in nums:
        if i not in seen:
            seen[i] = 1
        else:
            seen[i] += 1

    for j in seen:
        if seen[j] > 1:
            return True
    return False 

print(check_duplicate([1, 2, 3, 3])) 
print(check_duplicate([1, 2, 3, 4])) 
print(check_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])) 
print(check_duplicate([1, 2, 3, 1])) 


