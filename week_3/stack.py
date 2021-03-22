class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        head = Node(value)
        head.next = self.head
        self.head = head

    def printAll(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def pop(self):
        if self.is_empty():
            return "Empty Stack"

        delNode = self.head
        self.head = self.head.next
        return delNode.data

    def peek(self):
        if self.is_empty():
            return "Empty Stack"

        return self.head.data

    def is_empty(self):
        return self.head is None
