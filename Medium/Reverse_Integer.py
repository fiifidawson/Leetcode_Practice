import math
"""
  Reverse 123: Taking into consideration the restrictions from the question.

  1. Last digit of a number can be obtained by performing the modulo division with 10.
  eg. 123 % 10 = 3 [3 = (x3)new integer]
  
  2. To remove the last digit from a number, perform the integer division with 10.  
  eg. 123 // 10 = 12 [12 = new integer]

  3. Last digit of a number can be obtained by performing the modulo division with 10.
  eg. 12 % 10 = 2 [2 = (x2)new integer]

  4. Shit the 3 in (1.) to the left by one by multiplying it by 10.
  eg. 3 x 10 = 30

  5. Add the 2 from (3.)
  eg. x3 + x2
      30 + 2 = 32

When programming set the limits
MIN = -2^31 [-214783648]
MAX = 2^31 - 1 [+214783647]

Reverse everything exclusive of the last digit and compare with MIN and MAX
Get rid of the last digit by dividing(/) by 10


"""
class Solution:
    def reverse(self, x):
        # Integer.MAX_VALUE = 2147483647 (end with 7)
        # Integer.MIN_VALUE = -2147483648 (end with -8)

        MIN = -2147483648 # -2^31
        MAX = 2147483647 # 2^31 - 1

        res = 0
        # While integer x is not 0
        while x:
            # moding x by 10
            digit = int(math.fmod(x, 10))
            x = int(x/10) # Dividing by 10 and casting back as integer

            if (res > MAX // 10 or (res == MAX // 10 and digit >= MAX % 10)):
                return 0
            if (res < MIN // 10 or (res == MIN // 10 and digit <= MIN % 10)):
                return 0
            res = (res * 10) + digit
        return res
    




class Solution:
    def reverse(self, x: int) -> int:
        # Store the original input value in a variable m
        m = x
        # Convert the input value to a positive integer using abs()
        x = abs(x)
        # Convert the positive integer to a string, reverse it, and convert back to an integer
        x = int(str(x)[::-1])
        # Check if the reversed integer is within the valid range of a 32-bit signed integer
        if x > -2 ** 31 and x < 2 ** 31 - 1:
            # If the original input was negative, return the reversed integer with a negative sign
            if m < 0:
                return -x
            # If the original input was positive, return the reversed integer
            else:
                return x
        # If the reversed integer is not within the valid range, return 0
        else:
            return 0




class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            flipped = -1*int(str(x)[1:][::-1])
            if flipped < -2**31:
                return 0
            return -1*int(str(x)[1:][::-1]) 
        else:
            flipped = int(str(x)[::-1])
            if flipped >= 2**31:
                return 0
            return int(str(x)[::-1])





class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0

        while x != 0:
            rev = rev * 10 + x % 10
            x = x // 10

        if rev * sign < -2 ** 31 or rev * sign > 2 ** 31 - 1:
            return 0

        return rev * sign
    




class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            n = -1 * x
        else:
            n = x

        res = str(n)[::-1]
        res = int(res)

        if res > 2**31:
            return 0

        if x < 0:
            return -1 * res
        else:
            return res


            
            