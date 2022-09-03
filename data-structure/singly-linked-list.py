class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def print_list(self) -> None:
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def append(self, data) -> None:
        n = Node(data)
        if self.head is None:
            self.head = n
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = n

    def prepend(self, data) -> None:
        n = Node(data)
        n.next, self.head = self.head, n

    def insert_after_node(self, prev_node, data) -> None:
        if not prev_node:
            print("Previous node doesn't exist.")
            return

        n = Node(data)
        n.next = prev_node.next
        prev_node.next = n

sllist = LinkedList()
sllist.append("A")
sllist.append("B")
sllist.append("C")
sllist.prepend("D")
sllist.print_list()
sllist.insert_after_node("E")