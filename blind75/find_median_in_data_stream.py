'''
[2,3,4] => mid is .
'''

class MedianFinder:

    def __init__(self):
        self.stream = list()
        

    def addNum(self, num: int) -> None:
        self.stream.append(num)

    def findMedian(self) -> float:
        stream_len = len(self.stream)
        
        if stream_len % 2 == 1: # odd
            mid = stream_len / 2
            print("mid for even", mid)
            return self.stream[int(stream_len/2)]
        else:
            mid = int(stream_len / 2)
            print("mid for even", mid)
            return self.stream[mid] + self.stream[mid-1] / 2

if __name__ == '__main__':
    medianFinder = MedianFinder()
    medianFinder.addNum(1)
    medianFinder.addNum(2)
    print(medianFinder.findMedian())
    medianFinder.addNum(3)
    print(medianFinder.findMedian())