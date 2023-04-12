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
from typing import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check if the length of the strings are the same
        if len(s) != len(t):
            return False
        #create a hashmap for each string
        countS, countT = {}, {}

        #Build the hashmap
        #iterate through each string and add the characters to the hashmap
        for i in range(len(s)):
            #count the occurences of each character at index i 
            countS[s[i]] = 1 + countS.get(s[i], 0)#if the character is not in the hashmap, add it with a value of 1
            countT[t[i]] = 1 + countT.get(t[i], 0)#if the ch+9aracter is not in the hashmap, add it with a value of 1
            #get() returns the value of the key, if the key does not exist, it returns the default value 0

        #Iterate through the hashmap and compare the values
        #c = key
        for c in countS:
            if countS[c] != countT.get(c, 0):#if the value of the key in countS is not equal to the value of the key in countT
                return False
        return True




# Shortcut
#Counter() returns a dictionary with the keys being the elements of the list and the values being the number of times the element appears
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)



# Solution 2: Sorting
# Time Complexity: O(nlogn)
# Space Complexity: O(1) (less memory)
"""
Sort the strings and compare them
Sorting takes some extra memory, but it is a lot faster than the hashmap solution
Example
Test 1: anagram
sorted: aagmnr
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check if the length of the strings are the same
        if len(s) != len(t):
            return False
        #sort the strings
        s = sorted(s)
        t = sorted(t)
        #compare the strings
        return s == t