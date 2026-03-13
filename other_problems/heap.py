class MinHeap:
    def __init__(self):
        self.heap = []
        self.current_len = 0
        return

    def right_child(self, i):
        return self.heap[(i*2)+1]
    
    def left_child(self, i):
        return self.heap[(i*2)]

    def parent(self, i):
        return self.heap[(i-1)//2]
    
    def getMin(self):
        self.heap[0] if self.heap[0] else None

    def extractMin(self):
        min_value = self.heap[0]
        self.heap[0], self.heap[self.current_len-1] = self.heap[self.current_len-1], self.heap[0]
        
        self.heap = self.heap[:self.current_len-2]

        self.heapify()
        self.current_len = self.current_len - 1
        return min_value
    
    def heapify(self):
        i = len(self.heap)-1
        parent = self.parent(i)

        while (i > 0 and self.heap[i] > self.heap[parent]):
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = i - 1
            parent = self.parent(i)

def main():
    minHeap = MinHeap()

if __name__ == "__main__":
    main()