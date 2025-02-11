import collections


class Solution:
    def maxSlidingWindow(self, nums, k):
        output = []  # Initialize empty list for output
        q = collections.deque()  # Initialize a deque (double-ended queue) to store the indices of the elements in window
        l = r = 0  # Initialize two pointers to represent the left and right boundaries of the window

        while r < len(nums):  # while the right pointer is within the bounds of the list
            # pop smaller values from q
            # If the current element nums[r] is larger than the element at the last index of the deque
            # it means that the last element cannot be a maximum of any future windows, so we pop it from the deque
            while q and nums[q[-1]] < nums[r]:  
                q.pop()
            q.append(r)  # append the current index to the deque

            # remove left val from window
            # If the left pointer is larger than the first element in the deque
            # it means this element is no longer within the window, so we pop it from the deque
            if l > q[0]:  
                q.popleft()

            # If the current window has reached its maximum size (k), 
            # then add the maximum (nums[q[0]]) to the output list,
            # and move the left pointer to the right to start the new window
            if (r + 1) >= k:  
                output.append(nums[q[0]])
                l += 1
            r += 1  # move the right pointer to the right to expand the window

        return output  # Return the output list, which contains the maximums of all windows

