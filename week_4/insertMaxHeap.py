class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        curIndex = len(self.items) - 1

        while curIndex > 1:
            parentIndex = curIndex // 2
            if self.items[curIndex] > self.items[parentIndex]:
                self.items[curIndex], self.items[parentIndex] = self.items[parentIndex], self.items[curIndex]
                curIndex = parentIndex
            else:
                break


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!