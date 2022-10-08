class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return head

        cur = head
        l = 1
        while cur.next:
            cur = cur.next
            l += 1
        cur.next = head

        idx = l - k % l
        cur = head
        for _ in range(idx - 1):
            cur = cur.next
        newHead = cur.next
        cur.next = None

        return newHead
