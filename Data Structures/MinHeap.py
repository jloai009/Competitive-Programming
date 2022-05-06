class MinHeap:
    def __init__(self, array):
        self.heap = [None]
        for x in array:
            self.insert(x)

    def siftDown(self, i):
        x = self.heap[i]
        n = len(self.heap)
        while True:
            left = 2*i
            right = left + 1
            if (right < n and self.heap[right] < x and self.heap[right] < self.heap[left]):
                self.heap[i] = self.heap[right]
                i = right
            elif left < n and self.heap[left] < x:
                self.heap[i] = self.heap[left]
                i = left
            else:
                self.heap[i] = x
                return

    def siftUp(self, i):
        x = self.heap[i]
        while i > 1 and x < self.heap[i//2]:
            self.heap[i] = self.heap[i//2]
            i //= 2
        self.heap[i] = x

    def peek(self):
        return self.heap[1]

    def remove(self):
        root = self.heap[1]
        x = self.heap.pop()
        if len(self.heap) > 1:
            self.heap[1] = x
            self.siftDown(1)
        return root

    def insert(self, x):
        i = len(self.heap)
        self.heap.append(x)
        self.siftUp(i)