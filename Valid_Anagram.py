"""
An Anagram is a word or phrase formed by rearranging the letters
of a different word or phrase, typically using all the original 
letters exactly once.
"""
"""
Possible Considerations:
- t and s have the same length
- t and s have the same characters
- t and s have the same number of each character

"""


# Solution 1: Hashmap
# Time Complexity: O(n)
# Space Complexity: O(n) (Would need extra memory)
"""
Example
Test 1: anagram
value= character
key= number of times character appears
S                       T
Value|Key               Value|Key
  a  |  3                 a  |  3
  n  |  1                 n  |  1
  g  |  1                 g  |  1
  r  |  1                 r  |  1
  m  |  1                 m  |  1
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check if the length of the strings are the same
        if len(s) != len(t):
            return False
        #create a hashmap for each string
        countS, countT = {}, {}

        #iterate through each string and add the characters to the hashmap
        for i in range(len(s)):
            #count the occurences of each character at index i 
            countS[s[i]] = 1 + countS.get(s[i], 0)#if the character is not in the hashmap, add it with a value of 1
            countT[t[i]] = 1 + countT.get(t[i], 0)#if the character is not in the hashmap, add it with a value of 1
            #get() returns the value of the key, if the key does not exist, it returns the default value 0