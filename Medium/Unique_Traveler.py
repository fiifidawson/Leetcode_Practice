"""
In the Grid Traveler problem, we use dynamic programming (DP) 
with memoization to significantly improve the time complexity.

The problem itself is about finding the number of ways to travel 
from the top left of a m x n grid to the bottom right, moving only down or right. We can solve this using recursion, but this results in a lot of repeated calculations. By using a memo to store results, we avoid these repeated calculations and speed up the computation.

Time Complexity:
The time complexity of the problem is O(m*n). This is because in the worst-case scenario, 
each cell in the m x n grid is visited once. After a cell is visited, its result is stored in the memo,
and any future attempts to calculate it can simply look up the result in the memo, which is a
constant-time operation.

Space Complexity:
The space complexity is also O(m*n) because, in the worst-case scenario, we need to store the 
result of each cell in the memo. The memo is essentially a cache that has a key for each unique m, n pair. 
The maximum number of keys is the number of cells in the grid, which is m * n.

The other space consideration is the recursion stack. In the worst-case scenario, 
the depth of the recursion tree could be m + n (if the path travelled keeps switching between right and down),
which adds a O(m+n) space complexity. However, in Big O notation, we're often interested in the dominating term,
so we say the overall space complexity is O(m*n), which accounts for the space needed for the memo table.
"""

# Define a class named 'Solution'.
class Solution:
    
    # Within this class, define a function named 'uniquePaths' that takes 
    # three arguments: 'm', 'n', and 'memo'. The 'self' keyword refers 
    # to the instance of the class 'Solution'. 'm' and 'n' are integers,
    # and 'memo' is a dictionary with default value of an empty dictionary.
    # This function returns an integer.
    def uniquePaths(self, m: int, n: int, memo={}) -> int:
        
        # Create a string 'key' by formatting 'm' and 'n' as a string,
        # separating them with a comma. This key will be used to store and 
        # retrieve the number of unique paths for a specific grid size (m,n) in 'memo'.
        key = f"{m},{n}"
        
        # If 'key' is already in 'memo' (i.e., we've calculated the unique paths 
        # for this grid size before), return the corresponding value. This step 
        # allows us to use previously calculated results to avoid repeated computation, 
        # a technique called memoization.
        if (key in memo): return memo[key]

        # If 'm' or 'n' is 0, return 1. This case represents a degenerate grid 
        # (a line), for which there is only one possible path (along the line).
        if(m == 0 or n == 0): return 1

        # If 'm' or 'n' is 1, return 1. This case represents a grid of size 1xN 
        # or Mx1, for which there is also only one possible path (along the row or column).
        if(m == 1 or n == 1): return 1

        # If we reach this point, it means we haven't calculated the unique paths for 
        # the current grid size before and the grid is neither a line nor a single row/column.
        # In this case, we calculate it by making a recursive call to 'uniquePaths' function, 
        # once with 'm' decremented by 1 (representing a move downwards) and once with 'n' 
        # decremented by 1 (representing a move to the right), then adding these two results. 
        # This represents all possible paths from the top left to bottom right of the grid 
        # if only rightwards and downwards movements are allowed.
        # The result is then stored in 'memo' with 'key' for future reference.
        memo[key] = self.uniquePaths(m-1, n, memo) + self.uniquePaths(m, n-1, memo)

        # After the calculation, we return the result stored in 'memo' for the current 'key'.
        return memo[key]
