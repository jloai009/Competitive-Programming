class Heap:
    def __init__(self, items=[]):
        self.heap = [None]
        for x in items:
            self.push(x)

    def __len__(self):
        return len(self.heap)-1

    def push(self, x):
        self.heap.append(x)
        i = len(self.heap)-1
        while i > 1 and x < self.heap[i//2]:
            self.heap[i] = self.heap[i//2]
            i //= 2
        self.heap[i] = x

    def pop(self):
        root = self.heap[1]
        x = self.heap.pop()
        if self:
            i = 1
            n = len(self.heap)
            while True:
                left = i*2
                right = left + 1
                if right<n and self.heap[right]<=self.heap[left] and self.heap[right]<x:
                    self.heap[i] = self.heap[right]
                    i = right
                elif left<n and self.heap[left]<x:
                    self.heap[i] = self.heap[left]
                    i = left
                else:
                    self.heap[i] = x
                    break
        return root
