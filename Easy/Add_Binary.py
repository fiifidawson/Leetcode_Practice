"""
Add Binary:
Time Complexity: O(n), where n is the length of the longer input string. The code performs two conversions 
    from binary strings to integers, which take O(n) time each. The binary addition takes constant time. Finally, 
    the conversion back to binary string takes O(n) time. Therefore, the overall time complexity is O(n).
Space Complexity: O(n), where n is the length of the longer input string. The code creates a new string to 
    store the binary representation of the sum, which can have a maximum length of n+1 (if there is a carry in 
    the most significant bit). Therefore, the overall space complexity is O(n).
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Convert the binary strings to integers and add them
        toBin = bin(int(a,2) + int(b,2))
        
        # Return the binary representation of the sum as a string
        return toBin[2:]
