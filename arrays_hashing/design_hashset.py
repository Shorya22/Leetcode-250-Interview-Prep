"""
LeetCode Problem: Design HashSet
--------------------------------
Design a HashSet without using any built-in hash table libraries.

Implement the MyHashSet class:

Methods:
    - add(key): Inserts the value 'key' into the HashSet.
    - contains(key): Returns True if 'key' exists in the HashSet, else False.
    - remove(key): Removes the value 'key' from the HashSet. 
                   If 'key' does not exist, do nothing.

Example:
    Input:
        ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
        [[], [1], [2], [1], [3], [2], [2], [2], [2]]

    Output:
        [null, null, null, true, false, null, true, null, false]

    Explanation:
        myHashSet = MyHashSet()
        myHashSet.add(1)       # set = [1]
        myHashSet.add(2)       # set = [1, 2]
        myHashSet.contains(1)  # returns True
        myHashSet.contains(3)  # returns False (not found)
        myHashSet.add(2)       # set = [1, 2]
        myHashSet.contains(2)  # returns True
        myHashSet.remove(2)    # set = [1]
        myHashSet.contains(2)  # returns False (already removed)

Constraints:
    - 0 <= key <= 1,000,000
    - At most 10,000 calls will be made to add, remove, and contains.
"""

# Method 1: 
class MyHashSet:

    def __init__(self):
        self.data = []

    def add(self, key: int) -> None:
        if key not in self.data:
            self.data.append(key)
        
    def remove(self, key: int) -> None:
        if key in self.data:
            self.data.remove(key)
        
    def contains(self, key: int) -> bool:
        if key in self.data:
            return True
        else:
            return False
        
# Method 2:
class MyHashSet:

    def __init__(self):
        self.data = [False]*100001

    def add(self, key: int) -> None:
        self.data[key] = True

    def remove(self, key: int) -> None:
        self.data[key] = False

    def contains(self, key: int) -> bool:
        return self.data[key]
        

# Method 3:
class MyHashSet:

    def __init__(self):
        self.size = 10000
        self.table = [[] for _ in range(self.size)]

    def calculate_hash_value(self,key: int):
        return key % self.size

    def add(self, key: int) -> None:
        hv = self.calculate_hash_value(key)
        if key not in self.table[hv]:
            self.table[hv].append(key)

    def remove(self, key: int) -> None:
        hv = self.calculate_hash_value(key)
        if key in self.table[hv]:
            self.table[hv].remove(key)

    def contains(self, key: int) -> bool:
        hv = self.calculate_hash_value(key)
        return key in self.table[hv]

