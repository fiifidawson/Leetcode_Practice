import math

class Solution:
    def mySqrt(self, x: int) -> int:
        x = abs(x)
        return math.floor(math.sqrt(x))