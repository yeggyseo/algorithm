class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def printAll(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def append(self, data):
        cur = self.head

        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)

    def get_node(self, index):
        cur = self.head
        i = 0

        while i < index:
            cur = cur.next
            i += 1

        return cur

    def add_node(self, index, data):
        newNode = Node(data)

        if index == 0:
            newNode.next = self.head
            self.head = newNode
            return

        prev = self.get_node(index - 1)
        nxt = prev.next
        prev.next = newNode
        newNode.next = nxt

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return

        prev = self.get_node(index - 1)
        prev.next = prev.next.next



l = LinkedList(3)
l.append(4)
l.append(5)
l.append(6)
l.append(7)
l.append(8)
l.append(9)
l.add_node(5, 1)

l.delete_node(0)

l.printAll()

