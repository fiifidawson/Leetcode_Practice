class Solution:
    def findMin(self, nums):
        # Check if the array is empty, return -1 if true
        if len(nums) == 0:
            return -1
        # Check if the array has only one element, return that element if true
        if len(nums) == 1:
            return nums[0]

        # Initialize left and right pointers for binary search
        left = 0
        right = len(nums) - 1

        # Perform binary search
        while left < right:
            # Calculate the midpoint
            midpoint = left + (right - left) // 2
            
            # Check if the current element is smaller than the previous one
            if midpoint > 0 and nums[midpoint] < nums[midpoint - 1]:
                return nums[midpoint]
            # Check if the left part is sorted and right part contains the minimum
            elif nums[left] <= nums[midpoint] and nums[midpoint] > nums[right]:
                left = midpoint + 1
            # Otherwise, search in the left part
            else:
                right = midpoint - 1

        # Return the minimum element found
        return nums[left]
