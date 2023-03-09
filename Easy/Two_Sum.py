"""Brute Force Approach"""
"""Time Complexity: O(N)
   Space Complexity: O(N)
"""

"""
Clue:
The value we're looking for is the difference between the target and the current value
Once we know the value we're looking for, we can check if it exists in the list using 
a hashmap

Input: nums = [2,1,5,3], target = 4
            
    [ 2,   1,   5,   3]
      4-2, 4-1, 4-5, 4-3
      =2,  =3,  =-1, =1
      1 (at index 1) + 3 (at index 3) = 4
      That was the purpose of differentiating everything before 
      we put it into the hashmap (to make it easier to find the value we're looking for)
      

The hashmap can initially be empty
then iterate through the array in one pass

        Hashmap
        Key|Value
        2  |  0
        1  |  1
        5  |  2
        3  |  3
"""

class Solution:
    def twoSum(self, nums, target):
        prevMap = {} #value: index
        #Index, Value
        for i, n in enumerate(nums):
            # Check if the value we're looking for is in the hashmap
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            # If the value we're looking for is not in the hashmap
            # add the current value to the hashmap
            prevMap[n] = i
        return []
