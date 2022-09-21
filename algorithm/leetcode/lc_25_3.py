def reverseKGroup(self, head, k):
	dummy = jump = ListNode(0)
	dummy.next = l = r = head

	while True:
		i = 0
		while r and i < k:
			r = r.next
			i += 1

		if i == k: # satisfied, reverse the inner linked list
			cur, prev = l, r
			for _ in range(k):
				cur.next, prev, cur = prev, cur, cur.next
			jump.next, jump, l = prev, l, r
		else:
			return dummy.next

