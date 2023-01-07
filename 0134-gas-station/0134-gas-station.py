class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        surplus = 0
        start = 0
        
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            surplus += gas[i] - cost[i]
            if surplus < 0:
                start = i+1
                surplus = 0
                
        if total < 0 or start == len(gas):
            return -1
        else:
            return start
                