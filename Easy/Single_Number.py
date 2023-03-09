"""Single Number:
Time Complexity: O(n), where n is the number of elements in the input list. The code has to iterate 
    through all the elements in the list once to find the single number.
Space Complexity: O(1). The code only uses constant extra space to store a single variable (res)
    regardless of the size of the input list.

    XOR
    0 ^ 0 = 0
    0 ^ 1 = 1
    1 ^ 0 = 1
    1 ^ 1 = 0
"""

class Solution:
    def singleNumber(self, nums):
        res = 0 # Initialize the result to 0
        for n in nums: # Iterate through each number in the input list
            res = n ^ res # XOR the current number with the result
        return res # Return the result after all numbers have been XORed
