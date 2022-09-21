# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        k = 3

        dummy -> 1 -> 2 -> 3 -> 4 -> 5
        |   			   |
        p       		  cur
        """
        dummy = ListNode
        dummy.next = head
        prev, cur = dummy, dummy

        while cur.next is not None:
            i = 0
            while cur and i < k:
                cur= cur.next
                i += 1
            if i < k:
                break

            next = cur.next
            cur.next = None
            start = prev.next
            prev.next = None

            prev.next = self.reverse(start)
            start.next = next

            # important!
            prev = start
            cur = start
        return dummy.next


    def reverse(self, head, prev=None):
        if not head:
            return prev
        n = head.next
        head.next = prev
        return self.reverse(n, head)
