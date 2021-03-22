class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        n = Node(value)
        if self.is_empty():
            self.head = n
            self.tail = n
            return

        self.tail.next = n
        self.tail = n

    def dequeue(self):
        if self.is_empty():
            return "Empty Queue"

        n = self.head
        self.head = self.head.next

        return n.data


    def peek(self):
        if self.is_empty():
            return "Empty Queue"
        return self.head.data

    def is_empty(self):
        return self.head is None

    def printAll(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)


q.printAll()