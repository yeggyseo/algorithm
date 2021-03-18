# gets kth node from the last node in a linked list
# two pointer approach

# O(n) time


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        s = self.head
        e = self.head

        for i in range(k):
            e = e.next

        while e is not None:
            s = s.next
            e = e.next

        return s


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
# linked_list.append(4)
# linked_list.append(5)
# linked_list.append(8)
# linked_list.append(1)

print(linked_list.get_kth_node_from_last(2).data)
