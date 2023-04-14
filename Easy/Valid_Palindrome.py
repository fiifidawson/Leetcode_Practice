"""
Method 1
Uses extra memory: 
Time complexity: O(N) #newStr and reversed newStr
Space complexity: O(N)
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # building a new string to remove all
        # non-alphanumeric characters
        newStr = "" 

        # iterate throught the string
        for c in s:
            # check if each character is alpha numeric
            if c.isalnum():
                # if each character is alphanumeric, convert to lower case
                # and add to newStr
                newStr += c.lower()
        # comparing original string to reversed string
        return newStr == newStr[::-1]
        



"""
Method 2
Two Pointers: Moving from left to rigth simultaneously 
Time complexity: O(N)
Space complexity: O(1)
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # left pointer(l = 0) and right pointer(r = length of string)
        l, r = 0, len(s) - 1

        # checking whether its a palindrome whilst left pointer
        # is less than right pointer
        while l < r:
            #cheking whether characters are alhpanumeric
            # left character is not alphanumeric [boundary]
            while l < r and not self.alphaNum(s[l]):
                l += 1 #increment 
            while r > l and not self.alphaNum(s[r]):
                r -= 1 #decrment

            #comparing characrters
            #at position left and position right
            if s[l].lower() != s[r].lower():
                return False
            #Updating left and right pointers
            l, r = l+1, r-1

            
        return True
        

    #Alphanumeric function
    def alphaNum(self, c):
        #getting ASCII values 
        return(ord('A') <= ord(c) <= ord('Z') or #checking if its uppercase
               ord('a') <= ord(c) <= ord('z') or #checking if its lower case
               ord('0') <= ord(c) <= ord('1'))   #checking if its 0 to 9
    



class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward_striped_s = [c for c in s.lower() if c.isalnum()]
        backward_striped_s = forward_striped_s[::-1]
        return forward_striped_s == backward_striped_s
    




class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").lower()
        return s == s[::-1]