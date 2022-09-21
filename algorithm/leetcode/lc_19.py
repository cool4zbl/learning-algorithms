

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    """
    n = 2
    1 -> 2 -> 3 -> 4 -> 5
    |
    head
    # become
    1 -> 2 -> 3 -> 5
    |
    head

    # == STEP ==
    # len=5, n=2, which is (5-2+1)th=4th (base 1), prev one is 5-2 = 3 (base 1), which means we move 3 times to find prev one

    # use dummy to delete `head` handily
    # whole len(SLL) = len + 1, we need to find the (len-n)th node, so the fast one need to move `len(SLL) - (len - n) = len + 1 - (len - n) = 1 + n` steps

    # so if we want to move
            head
             |
    dummy -> 1 -> 2 -> 3 -> 4 -> 5
    |
    fast
    slow

    # after `fast` move `n+1` steps
            head
            |
    dummy -> 1 -> 2 -> 3 -> 4 -> 5
    |                  |
    slow             fast

    # slow & fast move at the same time until fast is None
            head
             |
    dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> None
                       |              |
                       slow           fast

    # slow.next = slow.next.next
            head
             |
    dummy -> 1 -> 2 -> 3 -> 5 -> None
                       |          |
                       slow       fast
    """
