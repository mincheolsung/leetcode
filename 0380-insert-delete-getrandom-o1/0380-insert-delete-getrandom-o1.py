class RandomizedSet:
    def __init__(self):
        self.values = []
        self.position = {}

    def insert(self, val: int) -> bool:
        if val not in self.position:
            self.values.append(val)
            self.position[val] = len(self.values)-1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.position:
            index = self.position[val]
            self.values[index] = self.values[-1]
            self.position[self.values[-1]] = index
            self.values.pop()
            del self.position[val]
            return True
        return False

    def getRandom(self) -> int:
        index = random.randrange(0,len(self.values))
        return self.values[index]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()