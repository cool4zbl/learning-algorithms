"""
    https://leetcode.com/problems/palindrome-linked-list/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True

        fast, slow = head

        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next

        """
            start reversing from the `slow.next` pointer
            get the new `head` pointer of the reversed list
            then assign the new `head` pointer to `slow`
        """
        slow = self.reverseList(slow.next)

        """
            compare the head and slow head list
        """
        while slow:
            if slow.val != head.val:
                return False
            slow = slow.next
            head = head.next

        return True

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, prev = None
        while cur:
            cur.next, prev, cur = prev, cur, head.next

            # next = head.next
            # head.next = prev
            # prev = head
            # head = next
        return prev
