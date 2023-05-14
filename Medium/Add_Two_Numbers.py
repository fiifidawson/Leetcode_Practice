from tkinter.tix import ListNoteBook


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        dummy = ListNode() # Dealing with the edge case of inserting into the the linkedlist
        curr = dummy # Current pointer pointing at the position where we would be inserting the new node
        
        carry = 0 # Carry over value

        # While either of them has a digit
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0 # If l1 is not None, then v1 is l1.val, otherwise v1 is 0
            v2 = l2.val if l2 else 0 # If l2 is not None, then v2 is l2.val, otherwise v2 is 0

            # new digit is the sum of the two digits plus the carry over value
            val = v1 + v2 + carry

            carry = val // 10 # Carry over value is the quotient of the new digit divided by 10
            val = val % 10 # New digit is the remainder of the new digit divided by 10
            curr.next = ListNode(val) # Insert the new digit into the linkedlist

            # Update the pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next # Return the linkedlist without the dummy node