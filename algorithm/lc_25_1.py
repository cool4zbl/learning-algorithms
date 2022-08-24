from __future__ import print_function

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

	def print_list(self):
		temp = self
		while temp is not None:
			print(temp.value, end=" ")
			temp = temp.next
		print()


def reverse_every_k_elements(head, k):
	dummy = Node()
	dummy.next = head
	prev, cur = dummy, head

	"""
	k = 2
				 start
				 	 |
	dummy -> 1 -> 2 -> 3 -> 4 -> 5
	|        |    |    |
	p		    cur

								start
									|
	dummy   None <- 1 <- 2 -> 3 -> 4 -> 5
	|                    |    |    |
	p		                temp  cur

							start
								|
	dummy -> 2 -> 1 -> 3 -> 4 -> 5
	|        |         |
	p		     temp      cur
	"""

	while True:
		i = 0
		temp = None
		start = prev.next
		while cur and i < k:
			cur.next, temp, cur = temp, cur, cur.next
			i += 1

		prev.next = temp
		start.next = cur

		prev = start

		if not cur:
			break

	return dummy.next


def reverse(head, prev=None):
	if not head:
		return prev
	n = head.next
	head.next = prev
	return reverse(n, head)


def main():
	head = Node(1)
	head.next = Node(2)
	head.next.next = Node(3)
	head.next.next.next = Node(4)
	head.next.next.next.next = Node(5)
	head.next.next.next.next.next = Node(6)
	#head.next.next.next.next.next.next = Node(7)
	#head.next.next.next.next.next.next.next = Node(8)

	print("Nodes of original LinkedList are: ", end='')
	head.print_list()
	result = reverse_every_k_elements(head, 3)
	print("Nodes of reversed LinkedList are: ", end='')
	result.print_list()


main()

