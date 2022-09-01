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

def reverseN(head, n):
	if n == 1:
		suc = head.next
		return head

	last = reverseN(head.next, n -1)
	head.next.next = head
	head.next = suc

	return last

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Solution 1, from list end to list start
    # assuming reversed all the nodes after head, starting from `head.next`, return the new head
    # then make head.next.next = head
    # head.next = None
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        temp = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return temp

    """

    """
    Solution 2, from list start to list end
    # we reverse the `head` first, make `head.next = prev`, prev = None in initial
    # then we reverse the remaind list recursively, prev = head, newHead = head.next
    """
    def reverseList(self, head: Optional[ListNode], prev=None) -> Optional[ListNode]:
        if not head:
            return prev

        n = head.next
        head.next = prev

        return self.reverseList(n, head)

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
	suc = None
	head.print_list()
	result = reverseN(head, 3)
	print("Nodes of reversed LinkedList are: ", end='')
	result.print_list()


main()