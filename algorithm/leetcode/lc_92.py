def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
     # p = left, q = right
     # 0. skip the p-1 nodes, reach p node
     # 1. remember p-1 node
     # 2. reverse p to q nodes
     # 3. connect p-1 and q+1 to reversed sub-list
     dummy = ListNode
     dummy.next = head

     # 0. skip the p-1 nodes, reach p node
     cur, prev = head, dummy
     i = 0
     while cur and i < left - 1:
         prev = cur
         cur = cur.next
         i += 1
     # after skipping 'p-1' nodes, `cur` will point to 'p'th node, `prev` point to 'p-1'th node

     # 1. remember p-1 node
     # we are interested in three parts of the LinkedList, the part before index 'p',
     # the part between 'p' and 'q', and the part after index 'q'
     last_n_of_first = prev

     # after reversing the LinkedList 'current' will become the last node of the sub-list
     last_n_of_sub = cur

     # 2. reverse nodes between 'p' and 'q'
     i = 0
     while cur and i < right - left + 1:
         cur.next, prev, cur = prev, cur, cur.next
         i += 1

     # 3.1 connect with first part
     last_n_of_first.next = prev
     # 3.2 connect with last part
     last_n_of_sub.next = cur

     # 4. return dummy list
     return dummy.next