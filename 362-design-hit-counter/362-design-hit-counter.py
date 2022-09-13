class HitCounter:
    def __init__(self):
        self.stamp = defaultdict(int)

    def hit(self, timestamp: int) -> None:
            self.stamp[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        num = 0
        for time,hit in self.stamp.items():
            if abs(timestamp - time) < 300:
               num+=hit
        return num
            


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)