import heapq

class PythonHeap:
    def __init__(self):
        self.myheap = []
        heapq.heapify(self.myheap)
    
    def getMin(self):
        return self.myheap[0]
    
    def insert(self, value):
        heapq.heappush(self.myheap, value)

    def extractMin(self):
        return heapq.heappop(self.myheap)

def main():
    pyHeap = PythonHeap()
    pyHeap.insert(10)
    pyHeap.insert(1)
    pyHeap.insert(11)
    pyHeap.insert(12)
    pyHeap.insert(2)
    print(pyHeap.extractMin())
    pyHeap.insert(3)
    pyHeap.insert(5)
    pyHeap.insert(6)
    print(pyHeap.extractMin())

if __name__ == '__main__':
    main()