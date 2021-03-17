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


def get_linked_list_sum(linked_list_1, linked_list_2):
    l1 = linkedListSumHelper(linked_list_1)
    l2 = linkedListSumHelper(linked_list_2)
    return l1 + l2


def linkedListSumHelper(linkedList):
    s = 0
    head = linkedList.head

    while head is not None:
        s = s * 10 + head.data
        head = head.next
    return s


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))
