"""
Time: O(m)
Space: O(M)
"""

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        res = defaultdict(list) # mapping charCount to List of Anagrams

        for s in strs:
            count = [0] * 26 # a.....z

            # Going through every character in each string
            for c in s:
               # mapping the characters
               count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)
        
        return res.values()
    