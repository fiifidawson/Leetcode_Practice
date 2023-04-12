class Solution:
    def isPalindrome(self, x: int) -> bool:
        # create a copy of x
        m = x
        # make x positive
        x = abs(x)
        #convert x to a string, reverse it, and convert it back to an integer
        x = int(str(x)[::-1])
        
        # check if reversed number is the same as original number
        if m == x:
            return True
        return False