"""
Invert a Binary Tree:
Time Complexity: O(n), where n is the number of nodes in the binary tree.
    The code has to visit every node in the tree once.
Space Complexity: O(h), where h is the height of the binary tree.
    The space complexity is equal to the maximum depth of the recursion stack, 
    which is equal to the height of the tree. In the worst case, the tree could 
    be skewed and have a height of n (i.e., the tree is a linked list), resulting 
    in a space complexity of O(n). However, in a balanced binary tree, the height is 
    logarithmic in terms of the number of nodes (i.e., h = log n), resulting in a space complexity of O(log n).

"""

class Solution:
    def invertTree(self, root):
        # Checking if root exists
        if not root:
            return None

        # Swapping the left and right child of the current node
        temp = root.left
        root.left = root.right
        root.right = temp

        # Recursively invert the left and right subtree
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Return the root of the inverted tree
        return root
