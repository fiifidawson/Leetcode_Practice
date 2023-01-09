"""
Method 1 [Brute Force]
Compare each number starting from first index to each other one at
a time.
time complexity: O(n^2)
space complexity: O(1)
"""

"""
Method 2 [Sorting]
Duplicates would be adjacent so iterating throught the array would 
be once.
time complexity:
     General: O(nlogn) 
     Sorting: O(n) {sorting - Hash Set/Map}
space complexity:
     General:  O(1)
     Sorting: O(n)
1. First sort
"""
List = [2, 3, 1, 5, 9, 1, 1, 9, 10, 5]

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
