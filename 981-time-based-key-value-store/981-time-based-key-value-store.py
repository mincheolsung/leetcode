class TimeMap:

    def __init__(self):
        self.time = defaultdict(list)
        self.values = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        time = self.time.get(key)
        if time == None:
            return ""

        values = self.values.get(key)
        i = bisect.bisect_right(time, timestamp)
        if i == 0:
            return ""
        else:
            return values[i-1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)