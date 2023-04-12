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
MIN = 2^31 [21]
MAX = 2^31 - 1


"""