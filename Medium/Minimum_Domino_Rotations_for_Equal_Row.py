""" Space Complexity: O(n)
    Time Complexity: O(n)

"""

class Solution:
    def minDominoRotations(self, tops, bottoms):
        # Initialize two variables to represent the first top and bottom values
        t1, t2 = tops[0], bottoms[0] 

        for target in [t1, t2]:
            missingT, missingB = 0, 0 

            # iterate through both arrays at the same time by using the zip function
            for i, pair in enumerate(zip(tops, bottoms)):
                top, bottom = pair
                if not (top == target or bottom == target):
                    break
                if top != target: missingT +=1
                if bottom != t1: missingB +=1
                if i == len(tops) - 1:
                    return min(missingT, missingB)
        return -1

