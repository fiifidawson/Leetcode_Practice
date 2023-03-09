"""
Binary Search:
Time Complexity: O(log n), where n is the number of elements in the input array. 
The code divides the search range in half at each step, resulting in a logarithmic time complexity.
Space Complexity: O(1). The code only uses constant extra space to store a few variables.
"""

class Solution:
    def search(self, nums, target: int) -> int:
        # Initialize the lower bound and upper bound of the search range
        low = 0
        high = len(nums) - 1
        
        # Continue searching as long as the search range is not empty
        while low <= high:
            # Calculate the middle index of the search range
            mid = (low + high) // 2
            
            # If the middle element is the target, return its index
            if target == nums[mid]:
                return mid
            
            # If the target is greater than the middle element, search the right half
            elif target > nums[mid]:
                low = mid + 1
                # Use 'continue' to skip the rest of the code in this iteration
                continue
            
            # If the target is less than the middle element, search the left half
            else:
                high = mid - 1
                # Use 'continue' to skip the rest of the code in this iteration
                continue
        
        # If the target is not found, return -1
        return -1
