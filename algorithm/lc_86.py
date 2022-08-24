# use objects
class ListNode:
	def __init__(self, data, next):
		self.val = data
		self.next = next

	def print_list(self):
		temp = self
		while temp is not None:
			print(temp.val, end=" ")
			temp = temp.next
		print()

y = None
# for i in range(6, 0, -1):
y = ListNode(1, y)
y = ListNode(4, y)

def partition(head: ListNode, x: int) -> ListNode:
	if not head:
		return head

	dummy, cur = ListNode, head
	l1 = dummy
	l2_start = ListNode
	l2 = l2_start

	while cur:
		if cur.val < x:
			l1.next = cur
			l1 = l1.next
		else:
			l2.next = cur
			l2 = l2.next

		cur = cur.next

	l1.next = l2_start.next

	return dummy.next

result = partition(y, 2)
y.print_list()
result.print_list()
