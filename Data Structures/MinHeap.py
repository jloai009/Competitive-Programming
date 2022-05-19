class MinHeap:
    def __init__(self, items=[]):
        self.heap = [None]
        for x in items:
            self.push(x)
            
    def __len__(self) -> int:
        return len(self.heap) - 1
    
    def push(self, x):
        self.heap.append(x)
        self.up()
        
    def up(self):
        i = len(self.heap)-1
        x = self.heap[i]
        while i > 1 and x < self.heap[i//2]:
            self.heap[i] = self.heap[i//2]
            i //= 2
        self.heap[i] = x
        
    
    def pop(self):
        if len(self.heap) <= 1:
            raise IndexError("Pop from empty MinHeap")
            
        root = self.heap[1]
        x = self.heap.pop()
        if self:
            self.heap[1] = x
            self.down()

        return root
    
    def down(self):
        i = 1
        x = self.heap[1]
        n = len(self.heap)
        
        while True:
            left = i*2
            right = left + 1
            if right < n and self.heap[right] < x and self.heap[right] < self.heap[left]:
                self.heap[i] = self.heap[right]
                i = right
            elif left < n and self.heap[left] < x:
                self.heap[i] = self.heap[left]
                i = left
            else:
                self.heap[i] = x
                return