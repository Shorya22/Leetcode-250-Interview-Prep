"""
Design HashMap

Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

- MyHashMap() initializes the object with an empty map.
- void put(int key, int value) inserts a (key, value) pair into the HashMap. 
  If the key already exists in the map, update the corresponding value.
- int get(int key) returns the value to which the specified key is mapped, 
  or -1 if this map contains no mapping for the key.
- void remove(key) removes the key and its corresponding value if the map 
  contains the mapping for the key.

Example 1:

Input: 
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]

Output: 
[null, null, null, 1, -1, null, 1, null, -1]

Explanation:
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1);      # The map is now [[1,1]]
myHashMap.put(2, 2);      # The map is now [[1,1], [2,2]]
myHashMap.get(1);         # return 1
myHashMap.get(3);         # return -1 (not found)
myHashMap.put(2, 1);      # update the existing value -> [[1,1], [2,1]]
myHashMap.get(2);         # return 1
myHashMap.remove(2);      # remove the mapping for 2 -> [[1,1]]
myHashMap.get(2);         # return -1 (not found)

Constraints:
0 <= key, value <= 1,000,000
At most 10,000 calls will be made to put, get, and remove.
"""

# Method 1:
class MyHashMap:

    def __init__(self):
        self.size = 1000001
        self.data = [-1 for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        self.data[key] = value

    def get(self, key: int) -> int:
        return self.data[key]

    def remove(self, key: int) -> None:
        self.data[key] = -1
        
# Method 2:
class MyHashMap:

    def __init__(self):
        self.size = 10000
        self.data = [[] for _ in range(self.size)]
        
    def calculate_hash_value(self,key: int):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        hv = self.calculate_hash_value(key)
        for i, (k,v) in enumerate(self.data[hv]):
            if k == key:
                self.data[hv][i] = (key,value)
                return
        self.data[hv].append((key,value))

    def get(self, key: int) -> int:
        hv = self.calculate_hash_value(key)
        for k,v in self.data[hv]:
            if k == key:
                return v
        return -1
        
    def remove(self, key: int) -> None:
        hv = self.calculate_hash_value(key)
        self.data[hv] = [(k,v) for (k,v) in self.data[hv] if k != key]
        