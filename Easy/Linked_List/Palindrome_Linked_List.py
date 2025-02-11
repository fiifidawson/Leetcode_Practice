


class Solution:
    def isPalindrome(self, head) -> bool:
        nums = []

        while head:
            nums.append(head.val)
            head = head.next


        l,r = 0, len(nums)-1
        while l<=r:
            if nums[l] != nums[r]:
                return False
            l+=1;r-=1
        return True
    


class Solution:
    def isPalindrome(self, head) -> bool:
        fast = head
        slow = head

        # find middle(slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second half
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                left = left.next
                right = right.next
        return True