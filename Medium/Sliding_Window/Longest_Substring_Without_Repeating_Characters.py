"""
Sets: Containly only one of each character
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        # initializing set
        charSet = set()

        # initializing sliding window
        l = 0

        res = 0

        # continuously change as every character is visited
        for r in range(len(s)):
            # While charecter at index r is inside in the set(its a duplicate)
            while s[r] in charSet:
                # Update the left char by removing it from the set
                # and increase it to the next index
                charSet.remove(s[l])
                l += 1
            # After removing all duplicates we can add the rightmost 
            # char to the set
            charSet.add(s[r])
            # update result is the current window size is larger than 
            # what it currently is
            res = max(res, r - l + 1) # the current substring's length (r - l + 1)
        return res