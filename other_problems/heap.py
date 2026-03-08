class MinHeap:
    def __init__(self):
        self.heap = []
        self.current_len = 0
        return
    
    def getMin(self):
        self.heap[0] if self.heap[0] else None

    def extractMin(self):
        min_val = self.heap[0]

        self.heap[0], self.heap[self.current_len-1] = self.heap[self.current_len-1], self.heap[0]
        self.heapify()
    
    def heapify(self):