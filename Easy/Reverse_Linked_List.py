"""
Reverse a Linked List:
Time Complexity: O(n), where n is the number of nodes in the linked list.
The code has to iterate through all the nodes in the linked list once.
Space Complexity: O(1). The code only uses constant extra space to store a few pointers.
"""

class Solution:
    def reverseList(self, head):
        # Initialize prev to None and curr to head
        prev, curr = None, head

        # Loop through the linked list
        while curr:
            # Store the next node of curr in nxt
            nxt = curr.next
            # Reverse the link between curr and prev
            curr.next = prev
            # Update prev and curr for the next iteration
            prev = curr
            curr = nxt
        # Return the new head of the reversed linked list
        return prev
