class MyCalendarThree:

    def __init__(self):
        self.timeline = []
        self.length = 0
        
    def book(self, start: int, end: int) -> int:
        insort_right(self.timeline, (start,1))
        insort_right(self.timeline, (end,-1))
        self.length+=2

        prefixSum = [0]*self.length
        prefixSum[0] = self.timeline[0][1]
        for i in range(1, self.length):
            prefixSum[i] = prefixSum[i-1] + self.timeline[i][1]

        return max(prefixSum)

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)