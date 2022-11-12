class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        if len(self.minHeap) == 0:
            heapq.heappush(self.minHeap, num)
            return

        if num < self.minHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)

        while len(self.minHeap) - len(self.maxHeap) > 1:
            item = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -item)

        while len(self.maxHeap) - len(self.minHeap) > 1:
            item = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, item)
            
    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0])/2
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return -self.maxHeap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()