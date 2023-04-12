""" 
Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "}": "{", "]": "["}

        for c in s:
            # if it is a closing parenthesis
            if c in closeToOpen:
                # Making sure stack is not empty and value at the top of the
                # stack is the corresponding opening parenthesis
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                # Parentheses don't match
                else:
                    return False
            # if it is an opening parenthesis
            else:
                stack.append(c)

        return True if not stack else False
    




# Define a class named Solution
class Solution:
    # Define a method named isValid which takes a string input 's' and returns a boolean value
    def isValid(self, s: str) -> bool:
        # Create a dictionary named 'hash_map' which maps closing parentheses to their corresponding opening parentheses
        hash_map = {')' : '(', ']' : '[', '}' : '{'}
        # Create an empty list named 'stack' which will be used as a stack data structure
        stack = []
        # Iterate over each character in the input string 's'
        for c in s:
            # Check if the current character 'c' is a closing parenthesis
            if c in hash_map:
                # If the stack is not empty and the top element of the stack is the corresponding opening parenthesis,
                # pop the top element from the stack
                if stack and stack[-1] == hash_map[c]:
                    stack.pop()
                # Otherwise, return False
                else:
                    return False
            # If the current character is not a closing parenthesis, it is an opening parenthesis, so append it to the stack
            else:
                stack.append(c)
        # Check if the stack is empty after processing the entire input string. If it is empty, return True. Otherwise, return False.
        return len(stack) == 0
